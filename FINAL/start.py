from keras.models import load_model
import numpy as np
import argparse
import dlib
import cv2
import tensorflow as tf
from pygame import mixer
from FINAL.logingui import data_get
import pyrebase
import time

sessionId,StudentId = data_get()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

model = tf.keras.models.load_model("my_model.h5")

ap = argparse.ArgumentParser()
ap.add_argument("-vw", "--isVideoWriter", type=bool, default=False)
args = vars(ap.parse_args())

from gaze_tracking import GazeTracking

gaze = GazeTracking()

emotion_offsets = (20, 40)
emotions = {
    0: {
        "emotion": "Angry",
        "color": (193, 69, 42)
    },
    1: {
        "emotion": "Disgust",
        "color": (164, 175, 49)
    },
    2: {
        "emotion": "Fear",
        "color": (40, 52, 155)
    },
    3: {
        "emotion": "Happy",
        "color": (23, 164, 28)
    },
    4: {
        "emotion": "Sad",
        "color": (164, 93, 23)
    },
    5: {
        "emotion": "Suprise",
        "color": (218, 229, 97)
    },
    6: {
        "emotion": "Neutral",
        "color": (108, 72, 200)
    }
}


def shapePoints(shape):
    coords = np.zeros((68, 2), dtype="int")
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords


def rectPoints(rect):
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    return x, y, w, h


faceLandmarks = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(faceLandmarks)

emotionModelPath = 'emotionModel.hdf5'
emotionClassifier = load_model(emotionModelPath, compile=False)
emotionTargetSize = emotionClassifier.input_shape[1:3]

mixer.init()
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
Score = 0

if args["isVideoWriter"]:
    fourrcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")
    capWidth = int(cap.get(3))
    capHeight = int(cap.get(4))
    videoWrite = cv2.VideoWriter("output.avi", fourrcc, 22,
                                 (capWidth, capHeight))

emotion_var = ''
drowsy_var = ''
eyeStatus = ''

#---------------------------------------------------------------------

firebaseConfig = {
    "apiKey": "AIzaSyAHBQ74fEHWetfupEFc0w0hjqWiaUDbw-0",
    "authDomain": "visagodb.firebaseapp.com",
    "databaseURL": "https://visagodb-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "projectId": "visagodb",
    "storageBucket": "visagodb.appspot.com",
    "messagingSenderId": "992480994037",
    "appId": "1:992480994037:web:2b4f44c6233fbdf65edbbc",
    "measurementId": "G-8E5RJZZ4VD"
}


firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


def calculateEngagement(db, sessionId, StudentId):
    global eyeStatus,lookAway,currentMood
    personalEngagementLv = 0
    moodEngagementLv = 0
    overrallEngagement = 0

    if eyeStatus == 'not sleep' and (lookAway == 'Looking center' or lookAway == "Blinking"):
        personalEngagementLv = 30
    elif eyeStatus == 'not sleep' and (lookAway == "Looking right" or lookAway == "Looking left"):
        personalEngagementLv = 20
    elif eyeStatus == 'sleep' and (lookAway == 'Looking center' or lookAway == "Blinking"):
        personalEngagementLv = 10
    elif eyeStatus == 'sleep' and (lookAway == "Looking right" or lookAway == "Looking left"):
        personalEngagementLv = 15

    if currentMood == "Happy":
        moodEngagementLv = 60
    elif currentMood == "Sad":
        moodEngagementLv = 50
    elif currentMood == "Angry":
        moodEngagementLv = 51
    elif currentMood == "Disgust":
        moodEngagementLv = 52
    elif currentMood == "Fear":
        moodEngagementLv = 53
    elif currentMood == "Suprise":
        moodEngagementLv = 54
    elif currentMood == "Neutral":
        moodEngagementLv = 55

    overrallEngagement = personalEngagementLv+moodEngagementLv

    # dictonary using to pass the engagement level to the db
    overrallEngagementUpdate = {"overall Engagement": overrallEngagement}

    engagement_update(db, sessionId, StudentId, overrallEngagementUpdate)


def engagement_update(db, sessionId, StudentId, engagement):
    db.child(sessionId).child(StudentId).update(engagement)


