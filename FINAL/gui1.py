import tkinter
from main import *
from guiproject import *

sessionId = 0

def login(lblsession=None):
    global sessionId
    sessionId = lblsession.get()

    print(sessionId)


def frame1():
    master = tkinter.Tk()
    master.geometry("390x350")

    bg_color = "DeepSkyBlue2"
    fg_color = "#383a39"
    master.configure(background=bg_color)
    master.title("Welcome")
    # -------username
    tkinter.Label(master, text="session id:", fg=fg_color, bg=bg_color,
                  font=("Helvetica", 15)).grid(row=8, padx=(50, 0), pady=(20, 10))

    lblsession = tkinter.Entry(master)
    lblsession.grid(row=8, column=1, padx=(10, 10), pady=(20, 10))

    # --------button
    tkinter.Button(master, text="submit", borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width=15,
                   command=lambda: [login(lblsession), master.destroy(), guisecond()]).grid(row=10, padx=(50, 0), pady=(20, 10))

    master.mainloop()

def check():
    print("fjvbibfr")