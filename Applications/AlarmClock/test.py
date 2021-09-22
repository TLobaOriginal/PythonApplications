import tkinter as ty
from tkinter import *
from tkinter import messagebox
import os, time, winsound
import tkinter

def createWidgets():
       #We use this to create a label and then we place the label on the 0th row
       label1 = Label(root, text="Enter in the time in hh:mm -")
       label1.grid(row = 0, column=0, padx=5, pady=5)

       #This will take user input. It acts as a text box
       global entry1 
       entry1 = Entry(root, width=15)
       entry1.grid(row=0, column=1)

       label2 = Label(root, text="Enter the message of alarm: ")
       label2.grid(row=1, column=0, padx=5, pady=5)

       global entry2
       entry2 = Entry(root, width=15)
       entry2.grid(row=1, column=1)

       but = Button(root, text="Submit", width=10, command=submit)
       but.grid(row=2, column=1)

       global label3
       label3 = Label(root, text="")
       label3.grid(row=3, column=1)

def message1():

       global entry1, label3
       AlarmTimeLabel = entry1.get()
       label3.config(text="The Alarm is Counting...") #We configure the text to say...
                                                      #The alarm clock is given a label
       messagebox.showinfo("Alarm Clock", f"The Alarm time: is {AlarmTimeLabel}")

def submit():

       global entry1, entry2, label3
       AlarmTime = entry1.get() 
       message1()
       currenttime =time.strftime("%H:%M") #We set the time to the current time
       alarmmessage = entry2.get()
       print(f"The Alarm time is: {AlarmTime}")

       while AlarmTime != currenttime:
              currenttime = time.strftime("%H:%M")
              time.sleep(1)

       if AlarmTime == currenttime: #When the right time is received then we play the alarm sound
              print("Playing Alarm Sound....")
              winsound.PlaySound("*", winsound.SND_ASYNC)
              label3.config(text="Alarm Sound Playing>>>>>")
              messagebox.showinfo("Alarm Message", f"The Message is: {alarmmessage}")



root = ty.Tk()
root.title("Alarm Clock")
root.geometry("400x150")


createWidgets()

root.mainloop()