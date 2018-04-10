
import numpy as np;
import time;
import RPi.GPIO as GPIO

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
def menu():
    print(".:Menu Options:.")
    print("1. Record")
    print("2. Play Music")
    print("3. Communicate")
    print("4. Quit")
    choice = raw_input("Select an option: \n");
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
            choice = raw_input("Select an option: \n");
            choice = choice.lower()
        

    
