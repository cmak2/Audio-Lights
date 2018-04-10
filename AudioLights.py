from tkinter import *
import numpy as np;
import time;
import RPi.GPIO as GPIO
import tkinter as tkint                    #Integrated Graphics Library
#import tkMessageBox

#7 Buttons
#7 Lights
#Record Sound/Lights from buttons (or mic)
#Play music from premade lists
#Communicate


#Define the Pins
pin1 = 21                   #A
pin2 = 22                   #B
pin3 = 23                   #C
pin4 = 24                   #D
pin5 = 25                   #E
pin6 = 26                   #F
pin7 = 27                   #G


#Processes Menu option
#GUI Menu
def guiMenu(top):
    menuLabel       = tkint.Label(top, text = ".:Menu Options:.")
    recordButton    = tkint.Button(top, text = "1. Record", command = record)
    playButton      = tkint.Button(top, text = "2. Play Music", command = play)
    commButton      = tkiny.Button(top, text = "3. Communicate", command = comm)
    quitButton      = tkint.Button(top, text = "4. Quit", command = qu)
    menuLabel.pack()
    playButton.pack()
    commButton.pack()
    quitButton.pack()
    initiate

#Basic Menu
def menu():
    
    print(".:Menu Options:.")
    print("1. Record")
    print("2. Play Music")
    print("3. Communicate")
    print("4. Quit")
    
    choice = input("Select an option: \n");
    choice = choice.lower()
    while True:
        if choice == "record" or choice == "1":
            print("Performing Step Operation")  #Placeholder
            time.sleep(1)
        elif choice == "play music" or choice == "2":
            print("Playing Music")              #Placeholder
            time.sleep(1)
        elif choice == "communicate" or choice == "3":
            print("Communicating...")           #Placeholder
            time.sleep(1)
        elif choice == "quit" or choice == "q" or choice == "4":
            return;
        else:
            print("Unknown Choice")
            choice = input("Select an option: \n");
            choice = choice.lower()    

def record():
    return
def play():
    return
def comm():
    return
def qu():
    quit()
    return

def initiate(top = tkint.Tk()):
    top.mainloop()

while True:
    print("Select an option:")
    print("1. Simple User Interface")
    print("2. Graphical User Interface")
    print("3. Quit")
    inp = input("Type in the option number to select: ")
    if inp == "1":
        menu()
    elif inp == "2":
        guiMenu(top = tkint.Tk())
    elif inp == "3":
        quit()
    else:
        print("Invalid option, please select one of the options.")


    
