from itertools import count
from time import sleep
from traceback import print_tb
from tracemalloc import start
from turtle import st
import pyrebase
from asyncio.windows_events import NULL


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


# take a function and update


users = db.child("12345").get()  # add the session ID

# print(type(users))

engagementValues = []
studentAttendance = []

for item in users.each():
    # test: check the overall engagement levels available in each session
    print(item.key(), item.val())
    engagementValues += [item.val()["overall Engagement"]]
    studentAttendance += [item.key()]


print("Engagement Values =", engagementValues)
print("Student Id's=", studentAttendance)

totalEngagement = 0
count = 0

for value in engagementValues:
    totalEngagement = totalEngagement+value
    count = count+1

overrallEngagement = totalEngagement/count
print("Class engagement level:", overrallEngagement)
