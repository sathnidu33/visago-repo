import sys
from keras.models import load_model
import numpy as np
import argparse
import dlib
import cv2
import tensorflow as tf
from pygame import mixer
import os

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

emotionModelPath = 'emotionModel.hdf5'  # fer2013_mini_XCEPTION.110-0.65
emotionClassifier = load_model(emotionModelPath, compile=False)
emotionTargetSize = emotionClassifier.input_shape[1:3]

mixer.init()
Score = 0


emotion_var = ''
drowsy_var = ''
eyeStatus = ''

def abc():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if args["isVideoWriter"]:
        fourrcc = cv2.VideoWriter_fourcc("M", "J", "P", "G")
        capWidth = int(cap.get(3))
        capHeight = int(cap.get(4))
        videoWrite = cv2.VideoWriter("output.avi", fourrcc, 22,
                                 (capWidth, capHeight))


    os.environ['OPENCV_VIDEOIO_PRIORITY_MSMF'] = '0'
    global Score,emotion_var,eyeStatus,drowsy_var
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (720, 480))

        if not ret:
            break

        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = detector(grayFrame, 0)
        for rect in rects:
            shape = predictor(grayFrame, rect)
            points = shapePoints(shape)
            (x, y, w, h) = rectPoints(rect)
            grayFace = grayFrame[y:y + h, x:x + w]
            try:
                grayFace = cv2.resize(grayFace, (emotionTargetSize))
            except:
                continue

            grayFace = grayFace.astype('float32')
            grayFace = grayFace / 255.0
            grayFace = (grayFace - 0.5) * 2.0
            grayFace = np.expand_dims(grayFace, 0)
            grayFace = np.expand_dims(grayFace, -1)
            emotion_prediction = emotionClassifier.predict(grayFace)
            emotion_probability = np.max(emotion_prediction)
            if emotion_probability > 0.36:
                emotion_label_arg = np.argmax(emotion_prediction)
                color = emotions[emotion_label_arg]['color']
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.line(frame, (x, y + h), (x + 20, y + h + 20),
                         color,
                         thickness=2)
                cv2.rectangle(frame, (x + 20, y + h + 20), (x + 110, y + h + 40),
                              color, -1)
                cv2.putText(frame, emotions[emotion_label_arg]['emotion'],
                            (x + 25, y + h + 36), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (255, 255, 255), 1, cv2.LINE_AA)
                realtime_predict = emotions[emotion_label_arg]['emotion']
                if emotion_var != realtime_predict:
                    emotion_var = realtime_predict
            else:
                color = (255, 255, 255)
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

        if args["isVideoWriter"]:
            videoWrite.write(frame)

        # -----------------------------------------------------------

        height, width = frame.shape[0:2]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
        eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

        cv2.rectangle(frame, (0, height - 50), (100, height), (0, 0, 0), thickness=cv2.FILLED)

        for (ex, ey, ew, eh) in eyes:
            # preprocessing steps
            eye = frame[ey:ey + eh, ex:ex + ew]
            eye = cv2.resize(eye, (80, 80))
            eye = eye / 255
            eye = eye.reshape(80, 80, 3)
            eye = np.expand_dims(eye, axis=0)
            # preprocessing is done now model prediction
            prediction = model.predict(eye)

            # if eyes are closed
            if prediction[0][0] > 0.30:
                cv2.putText(frame, 'closed', (10, height - 20), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1,
                            color=(255, 255, 255),
                            thickness=1, lineType=cv2.LINE_AA)

                Score = Score + 1
                if Score > 15:
                    try:
                        drowsy_var = 'sleep'
                    except:
                        pass

            # if eyes are open
            elif prediction[0][1] > 0.90:
                cv2.putText(frame, 'open', (10, height - 20), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1,
                            color=(255, 255, 255),
                            thickness=1, lineType=cv2.LINE_AA)
                Score = Score - 1
                if Score < 0:
                    Score = 0
                    drowsy_var = 'not sleep'

                    # ----------------------------------------------------------
        gaze.refresh(frame)

        frame = gaze.annotated_frame()

        if gaze.is_blinking():
            text = "Blinking"
            if eyeStatus != text:
                eyeStatus = text
        elif gaze.is_right():
            text = "Looking right"
            if eyeStatus != text:
                eyeStatus = text
        elif gaze.is_left():
            text = "Looking left"
            if eyeStatus != text:
                eyeStatus = text
        elif gaze.is_center():
            text = "Looking center"
            if eyeStatus != text:
                eyeStatus = text

        cv2.putText(frame, eyeStatus, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

        # left_pupil = gaze.pupil_left_coords()
        # right_pupil = gaze.pupil_right_coords()


        cv2.imshow('frame', frame)
        if cv2.waitKey(33) & 0xFF == ord('q'):
            break
        if sys.getsizeof(frame) > 20:
            cap.release()
            if args["isVideoWriter"]:
                videoWrite.release()
            cv2.destroyAllWindows()

            return

def data():
    return emotion_var,drowsy_var,eyeStatus
