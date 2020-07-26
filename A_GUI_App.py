import tkinter as tk
from tkinter import filedialog, Text
import os

apps = []
root = tk.Tk()

if os.path.isfile('your_work.txt'):
    with open("your_work.txt","r") as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        print(tempApps)
        apps = [x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select App", filetypes=(("Executebles (The Format that most apps are in)","*.exe"),("macOS Apps (For macOS Users)","*.app"),("All Files",".")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="#1EFF00", fg="Black")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=1080, width=2000, bg="#009DDF")
canvas.pack()

frame = tk.Frame(root, bg="#1EFF00")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Add App", padx=20, pady=10, fg="Black", bg="#009DFF", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run All Apps", padx=20, pady=10, fg="Black", bg="#009DFF", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app, bg="#1EFF00")
    label.pack()

root.mainloop()

with open("your_work.txt","w") as f:
    for app in apps:
        f.write(app + ",")