import RPi.GPIO as GPIO
from time import sleep
from robot_class import Robot
from lamps import *
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

leftIR = 14
middleIR = 15
rightIR = 18

buttonPin = 26
buttonstate = 1
started = False
stop = False
kruisingCount = 0
route = 0
draaitijdcount = 0
start = 0

print(route)

robot = Robot()


def kruispunt(route):  # In deze collectie van if statements wordt er gekeken welke route er is opgegeven.
    if (route == 1):  # 1 staat voor links.
        knipper_links()
        for x in range(0, 150):
            robot.linksaf()
        while (GPIO.input(middleIR)):
            robot.scherplinks()
    elif (route == 2):  # 2 staat voor rechtdoor.
        sleep(2)
        for x in range(0, 150):
            robot.rechtdoor()
    elif (route == 3):  # 3 staat voor rechts.
        knipper_rechts()
        for x in range(0, 150):
            robot.rechtsaf()
        while (GPIO.input(middleIR)):
            robot.scherprechts()
    else:
        print("no route to host")


GPIO.setup(leftIR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(middleIR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightIR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(21, GPIO.OUT)  # linker lichten
GPIO.setup(20, GPIO.OUT)  # worden de disco's
GPIO.setup(16, GPIO.OUT)  # rechter lichten

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(leftIR, GPIO.IN)  # GPIO 14 -> Left IR out
GPIO.setup(middleIR, GPIO.IN)  # GPIO 15 -> middle IR out
GPIO.setup(rightIR, GPIO.IN)  # GPIO 18 -> Right IR out

while not stop:

    file = open("start.txt", "r")  # Open en lees de inhoud van het bestand waar de route in staat.
    start = file.read()
    file.close()

    start = int(start)

    buttonstate = GPIO.input(buttonPin)
    if buttonstate == 0 or start == 1:  # Er wordt hier gekeken of de startbutton is ingedrukt of niet.

        file = open("direction.txt", "r")  # Open en lees de inhoud van het bestand waar de route in staat.
        route = file.read()
        file.close()

        route = int(route)

        print("Voor het starten, wat is mijn directie?", route)

        print("start")
        started = True
        GPIO.output(21, True)
        GPIO.output(16, True)
        while started:
            buttonstate = GPIO.input(buttonPin)
            curr_left = GPIO.input(leftIR)
            curr_middle = GPIO.input(middleIR)
            curr_right = GPIO.input(rightIR)

            if (curr_left == 0) and (curr_middle == 0) and (
                    curr_right == 1):  # Als deze condities waar zijn gaat de robot linksaf
                robot.linksaf()
                print("linksaf")
            elif (curr_left == 1) and (curr_middle == 0) and (
                    curr_right == 0):  # Als deze condities waar zijn gaat de robot rechtsaf
                robot.rechtsaf()
                print("rechtsaf")
            elif (curr_left == 0) and (curr_middle == 1) and (
                    curr_right == 1):  # Als deze condities waar zijn neemt de robot een scherpe linkse bocht
                print("scherplinks")
                for x in range(0, 20):
                    robot.scherplinks()
            elif (curr_left == 1) and (curr_middle == 1) and (
                    curr_right == 0):  # Als deze condities waar zijn neemt de robot een scherpe rechtse bocht.
                print("scherprechts")
                for x in range(0, 20):
                    robot.scherprechts()
            elif (curr_left == 0) and (curr_middle == 0) and (curr_right == 0):
                if (kruisingCount == 1):  # Hier wordt gekeken of 'Creamy' al een keer over een kruispunt gereden is.
                    started = False
                    stop = True
                    file = open("start.txt", "w")
                    file.write("0")
                    file.close
                    discolight()
                else:
                    kruispunt(route)
                    kruisingCount += 1
            else:  # Als de rest het allemaal niet is gaat de robot rechtdoor.
                robot.rechtdoor()

    sleep(.2)

GPIO.cleanup()
