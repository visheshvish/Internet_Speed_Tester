from tkinter import *
from tkinter import messagebox
import pyspeedtest


def one():
    speed = pyspeedtest.SpeedTest("www.google.com")
    a1 = (str(speed.download())+"[Bytes per second]" )
    messagebox.showinfo("Your Download Speed",a1)
root = Tk()
root.title("INTERNET SPEED TEST")
root.config(bg="#e4d2ce")
root.geometry("500x250")

label1 = Label(root, text ="Internet Speed Test",font=("Arial",30,"bold"),bg="lightblue").pack()
button1 = Button(root,text="Click !", font=("Arial",20,"bold"),bg="yellow", height = 1,width = 10,command=one).pack()


root.mainloop()
