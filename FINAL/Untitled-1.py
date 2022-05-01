from FINAL.logingui import data_get
from FINAL.final import *
import pyrebase
import time
print('ok')
currentMood,eyeStatus,lookAway = '','',''

sessionId,StudentId = data_get()
def threeData():
    abc()
    global currentMood,eyeStatus,lookAway
    currentMood,eyeStatus,lookAway = data()
    print(currentMood+eyeStatus+lookAway)

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

    if eyeStatus == 'not sleep' and (lookAway == 'Looking center' or lookAway == "Blinking"):
        personalEngagementLv = 50
    elif eyeStatus == 'not sleep' and (lookAway == "Looking right" or lookAway == "Looking left"):
        personalEngagementLv = 30
    elif eyeStatus == 'sleep' and (lookAway == 'Looking center' or lookAway == "Blinking"):
        personalEngagementLv = 10
    elif eyeStatus == 'sleep' and (lookAway == "Looking right" or lookAway == "Looking left"):
        personalEngagementLv = 10


    if currentMood == "Happy":
        moodEngagementLv = 50
    elif currentMood == "Sad":
        moodEngagementLv = 30
    elif currentMood == "Angry":
        moodEngagementLv = 50
    elif currentMood == "Disgust":
        moodEngagementLv = 20
    elif currentMood == "Fear":
        moodEngagementLv = 30
    elif currentMood == "Suprise":
        moodEngagementLv = 50
    elif currentMood == "Neutral":
        moodEngagementLv = 40

    overrallEngagement = personalEngagementLv+moodEngagementLv

    # dictonary using to pass the engagement level to the db
    overrallEngagementUpdate = {"overall Engagement": overrallEngagement}

    engagement_update(db, sessionId, StudentId, overrallEngagementUpdate)
    print(overrallEngagementUpdate)


def engagement_update(db, sessionId, StudentId, engagement):
    db.child(sessionId).child(StudentId).update(engagement)

try:
    while True:
        calculateEngagement(db=db, sessionId=sessionId, StudentId=StudentId)
        threeData()
        print("Updated")
        time.sleep(5)
except KeyboardInterrupt:
    pass
