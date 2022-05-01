import pyrebase
import time

sessionId = str(input("Enter the session Id:")).strip()
StudentId = int(input("Enter the StudentId:"))


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

    personalEngagementLv = 0
    eyesStatus = 0
    lookAway = 0
    currentMood = "happy"
    moodEngagementLv = 0
    overrallEngagement = 0

    if eyesStatus == 1 and lookAway == 1:
        personalEngagementLv = 30
    elif eyesStatus == 0 and lookAway == 1:
        personalEngagementLv = 0
    elif eyesStatus == 1 and lookAway == 0:
        personalEngagementLv = 40
    elif eyesStatus == 0 and lookAway == 0:
        personalEngagementLv = 35

    if currentMood == "happy":
        moodEngagementLv = 60
    elif currentMood == "sad":
        moodEngagementLv = 50
    elif currentMood == "angry":
        moodEngagementLv = 50
    elif currentMood == "disgust":
        moodEngagementLv = 50
    elif currentMood == "fear":
        moodEngagementLv = 50
    elif currentMood == "surprise":
        moodEngagementLv = 50
    elif currentMood == "neutral":
        moodEngagementLv = 50

    overrallEngagement = personalEngagementLv+moodEngagementLv

    # dictonary using to pass the engagement level to the db
    overrallEngagementUpdate = {"overall Engagement": overrallEngagement}

    engagement_update(db, sessionId, StudentId, overrallEngagementUpdate)


def engagement_update(db, sessionId, StudentId, engagement):
    db.child(sessionId).child(StudentId).update(engagement)


while True:

    calculateEngagement(db=db, sessionId=sessionId, StudentId=StudentId)
    print("Updated")
    time.sleep(5)
