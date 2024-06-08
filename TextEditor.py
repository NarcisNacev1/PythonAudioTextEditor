from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror
import speech_recognition as sr

filename = None

def newFile():
    global filename
    filename = "PythonTextEditor"
    text_widget.delete(0.0, END)

def saveFile():
    global filename
    if filename:
        t = text_widget.get(0.0, END)
        try:
            with open(filename, "w") as f:
                f.write(t.rstrip())
        except Exception as e:
            showerror(title="Error", message=f"Unable to save file: {e}")
    else:
        saveAs()

def saveAs():
    global filename
    f = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if f:
        filename = f.name
        t = text_widget.get(0.0, END)
        try:
            f.write(t.rstrip())
            f.close()
        except Exception as e:
            showerror(title="Error", message=f"Unable to save file: {e}")

def openFile():
    global filename
    f = filedialog.askopenfile(mode="r")
    if f:
        filename = f.name
        t = f.read()
        text_widget.delete(0.0, END)
        text_widget.insert(0.0, t)
        f.close()

def changeTextFont(font):
    font_dict = {
        "Arial": "Arial",
        "Helvetica": "Helvetica",
        "Verdana": "Verdana",
        "Georgia": "Georgia",
        "Calibri": "Calibri",
        "Palatino": "Palatino"
    }

    text_widget.config(font=font_dict.get(font, "Arial"))

def changeTextColor(color):
    color_dict = {
        "Red": "red",
        "Blue": "blue",
        "Green": "green",
        "Yellow": "yellow",
        "Purple": "purple",
        "Black": "black"
    }
    text_widget.config(foreground=color_dict.get(color, "black"))


def voiceTyping():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        text_widget.insert(END, text)
        print("Speech recognized:", text)
    except sr.UnknownValueError:
        showerror(title="Error", message="Speech recognition could not understand audio")
    except sr.RequestError as e:
        showerror(title="Error", message=f"Could not request results from Google Web Speech API service; {e}")


root = Tk()
root.title("PythonTextEditor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)
text_widget = Text(root, width=400, height=400)
text_widget.pack()

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)

fontmenu = Menu(menubar, tearoff=0)
fontmenu.add_command(label="Arial", command=lambda: changeTextFont("Arial"))
fontmenu.add_command(label="Helvetica", command=lambda: changeTextFont("Helvetica"))
fontmenu.add_command(label="Verdana", command=lambda: changeTextFont("Verdana"))
fontmenu.add_command(label="Georgia", command=lambda: changeTextFont("Georgia"))
fontmenu.add_command(label="Calibri", command=lambda: changeTextFont("Calibri"))
fontmenu.add_command(label="Palatino", command=lambda: changeTextFont("Palatino"))

menubar.add_cascade(label="Font", menu=fontmenu)

colormenu = Menu(menubar, tearoff=0)
colormenu.add_command(label="Red", command=lambda: changeTextColor("Red"))
colormenu.add_command(label="Blue", command=lambda: changeTextColor("Blue"))
colormenu.add_command(label="Green", command=lambda: changeTextColor("Green"))
colormenu.add_command(label="Yellow", command=lambda: changeTextColor("Yellow"))
colormenu.add_command(label="Purple", command=lambda: changeTextColor("Purple"))
colormenu.add_command(label="Black", command=lambda: changeTextColor("Black"))

# lambda is a specific function that will
# be called when something is clicked or
# something it waits for an input

menubar.add_cascade(label="Color", menu=colormenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Voice Typing", command=voiceTyping)
menubar.add_cascade(label="Edit", menu=editmenu)

root.config(menu=menubar)
root.mainloop()
