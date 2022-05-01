import tkinter as tk
from PIL import ImageTk, Image

master = tk.Tk()
master.geometry("390x350")
sessionId = ''
StudentId = ''


def login():
    global sessionId,StudentId
    sessionId = lblusername.get()
    StudentId = lblpassword.get()

def data_get():
    return sessionId, StudentId


bg_color = "DeepSkyBlue2"
fg_color = "#383a39"
master.configure(background=bg_color)
master.title("Welcome")
# ---heading image
photo = ImageTk.PhotoImage(Image.open("emo.jpg"))
tk.Label(master, image=photo).grid(rowspan=3, columnspan=5, row=0, column=0)
# -------username
tk.Label(master, text="Student ID :", fg=fg_color, bg=bg_color, font=("Helvetica", 15)).grid(row=8, padx=(50, 0),
                                                                                             pady=(20, 10))
lblusername = tk.Entry(master)
lblusername.grid(row=8, column=1, padx=(10, 10), pady=(20, 10))

# ----password
tk.Label(master, text="Session ID :", fg=fg_color, bg=bg_color, font=("Helvetica", 15)).grid(row=9, padx=(50, 0),
                                                                                             pady=(20, 10))
lblpassword = tk.Entry(master)
lblpassword.grid(row=9, column=1, padx=(10, 10), pady=(20, 10))

# --------button
tk.Button(master, text="Join Session", borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width=15,
          command=lambda: [login(), master.destroy()]).grid(row=10, padx=(50, 0), pady=(20, 10))

master.mainloop()
