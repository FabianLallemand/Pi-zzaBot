import RPi.GPIO as GPIO
from time import sleep
from robot_class import Robot
from lamps import *
from threading import Thread
import lamps

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

leftIR = 14
middleIR = 15
rightIR = 18

buttonPin = 26
buttonstate = 1
started = False
stop = False
route = 1
kruisingCount = 0

robot = Robot()

def kruispunt(route):
    if (route == 1):
        Thread(target=lamps.knipper_links())
        sleep(2)
        for x in range(0, 450):
            robot.linksaf()
    elif (route == 2):
        sleep(2)
        robot.rechtdoor()
    elif route == 3:
        Thread(target=lamps.knipper_rechts())
        sleep(2)
        for x in range(0, 450):
            robot.rechtsaf()
    else:
        print("no route to host")

GPIO.setup(leftIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(middleIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(21,GPIO.OUT) #linker lichten
GPIO.setup(20,GPIO.OUT) #worden de disco's
GPIO.setup(16,GPIO.OUT) #rechter lichten

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(leftIR,GPIO.IN) #GPIO 14 -> Left IR out
GPIO.setup(middleIR,GPIO.IN) #GPIO 15 -> middle IR out
GPIO.setup(rightIR,GPIO.IN) #GPIO 18 -> Right IR out

while not stop:

    buttonstate = GPIO.input(buttonPin)
    if (buttonstate == 0):
        print("start")
        started = True
        GPIO.output(21,True)
        GPIO.output(16,True)
        GPIO.output(20, True)
        while started:
            buttonstate = GPIO.input(buttonPin)
            curr_left = GPIO.input(leftIR)
            curr_middle = GPIO.input(middleIR)
            curr_right = GPIO.input(rightIR)

            if (curr_left == 0) and (curr_middle == 0) and (curr_right == 1):
                robot.linksaf()
                print("linksaf")
            elif (curr_left == 1) and (curr_middle == 0) and (curr_right == 0):
                robot.rechtsaf()
                print("rechtsaf")
            elif (curr_left == 0) and (curr_middle == 1) and (curr_right == 1):
                robot.scherplinks()
                print("scherplinks")
            elif (curr_left == 1) and (curr_middle == 1) and (curr_right == 0):
                robot.scherprechts()
                print("scherprechts")
            elif (curr_left == 0) and (curr_middle == 0) and (curr_right == 0):
                if (kruisingCount == 1):
                    started = False
                    stop = True
                else:
                    kruispunt(route)
                    kruisingCount += 1
            else:
                robot.rechtdoor()

    sleep(.2)


GPIO.cleanup()
