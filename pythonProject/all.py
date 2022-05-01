import time
import pyrebase
import tkinter
from tkinter import *
import tkinter as tk

value = True

def login(lblsession=None):
    global sessionId
    sessionId = lblsession.get()

def parseID():
    return sessionId

def frame1():
    master = tkinter.Tk()
    master.geometry("390x350")

    bg_color = "DeepSkyBlue2"
    fg_color = "#383a39"
    bt_color = "#fff"
    master.configure(background=bg_color)
    master.title("Welcome")
    # -------username
    tkinter.Label(master, text="session id:", fg=fg_color, bg=bg_color,
                  font=("Helvetica", 15)).grid(row=8, padx=(50, 0), pady=(20, 10))

    lblsession = tkinter.Entry(master)
    lblsession.grid(row=8, column=1, padx=(10, 10), pady=(20, 10))

    # --------button
    tkinter.Button(master, text="submit", borderwidth=2, relief='ridge', fg=fg_color, bg=bt_color, width=15,
                   command=lambda: [login(lblsession), master.destroy()]).grid(row=10, padx=(50, 0), pady=(20, 10))

    master.mainloop()

frame1()

#-------------------------------------------

def guisecond(engagement,attendance):
    top = Tk()
    top.geometry("450x300")

    bg_color = "DeepSkyBlue2"
    fg_color = "#383a39"
    bt_color = "#fff"
    top.configure(background=bg_color)

    t1 = Label(top, text="Attendence",fg=fg_color).place(x=40, y=60)
    t2 = Label(top, text="Engagement",fg=fg_color).place(x=40, y=100)

    a = str(attendance)
    b = str(round(engagement))


    t1 = Label(top, text=a).place(x=140, y=60)
    t2 = Label(top, text=b).place(x=140, y=100)

    def leave():
        global value
        value = False

    tkinter.Button(top, text="Stop", borderwidth=2, relief='ridge', fg=fg_color, bg=bt_color, width=15,
                   command=lambda: [leave(), top.destroy()]).grid(row=20, padx=(50, 0), pady=(150, 10))
    tkinter.Button(top, text="Refresh", borderwidth=2, relief='ridge', fg=fg_color, bg=bt_color, width=15,
                   command= top.destroy).grid(row=20, padx=(50, 0), pady=(200, 10))

    top.mainloop()
#-----------------------------------------------
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


while (value):
    # take a function and update

    users = db.child(parseID()).get()  # add the session ID

    # print(type(users))
    engagementValues = []

    for item in users.each():
        # test: check the overall engagement levels available in each session
        print(item.key(), item.val())
        engagementValues += [item.val()["overall Engagement"]]


    print("Engagement Values =", engagementValues)

    totalEngagement = 0
    count = 0

    for value in engagementValues:
        totalEngagement = totalEngagement+value
        count = count+1

    overrallEngagement = totalEngagement/count
    print("Class engagement level:", overrallEngagement)
    guisecond(overrallEngagement,count)
    if value == False:
        break


