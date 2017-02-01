import tkinter
import threading

from Sender import SendingThread
from KeyPressMap import KEYS


def keypress(event):
    KEYS.keyDown(event.keysym)

def keyrelease(event):
    KEYS.keyUp(event.keysym)

def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)

def focuslost(event):
    KEYS.allUp()

def setupKeyManager(frame):
    frame.bind("<KeyPress>", keypress)
    frame.bind("<Up>", keypress)
    frame.bind("<Down>", keypress)
    frame.bind("<Left>", keypress)
    frame.bind("<Right>", keypress)
    frame.bind("<KeyRelease>", keyrelease)
    frame.bind("<Button-1>", callback)
    frame.bind("<FocusOut>", focuslost)
    frame.pack()

    keyThread = threading.Thread(target=SendingThread)
    keyThread.daemon = True
    keyThread.start()


if __name__ == "__main__":

    root = tkinter.Tk()

    frame = tkinter.Frame(root, width=150, height=100)

    setupKeyManager(frame)
    
    
    mainLabel = tkinter.Label(root, text="Use wsad or arrow keys to move")

    mainLabel.pack()

    root.mainloop()
