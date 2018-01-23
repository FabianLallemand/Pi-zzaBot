import RPi.GPIO as GPIO
from time import sleep
from robot_class import Robot

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

leftIR = 14
middleIR = 15
rightIR = 18

buttonPin = 26
buttonstate = 1
started = False
stop = False
route = 2

robot = Robot()

def kruispunt(route):
    if (route == 1):
        for x in range(0, 100):
            robot.scherplinks()
    elif (route == 2):
        robot.rechtdoor()
    elif (route == 3):
        for x in range(0, 100):
            robot.scherprechts()
    else:
        print "no route to host"

GPIO.setup(leftIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(middleIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(leftIR,GPIO.IN) #GPIO 14 -> Left IR out
GPIO.setup(middleIR,GPIO.IN) #GPIO 15 -> middle IR out
GPIO.setup(rightIR,GPIO.IN) #GPIO 18 -> Right IR out

while not stop:

    buttonstate = GPIO.input(buttonPin)
    if (buttonstate == 0):
        print "start"
        started = True
        while started:
            buttonstate = GPIO.input(buttonPin)
            curr_left = GPIO.input(leftIR)
            curr_middle = GPIO.input(middleIR)
            curr_right = GPIO.input(rightIR)

            if (curr_left == 0) and (curr_middle == 0) and (curr_right == 1):
                robot.linksaf()
                print "linksaf"
            elif (curr_left == 1) and (curr_middle == 0) and (curr_right == 0):
                robot.rechtsaf()
                print "rechtsaf"
            elif (curr_left == 0) and (curr_middle == 1) and (curr_right == 1):
                robot.scherplinks()
                print "scherplinks"
            elif (curr_left == 1) and (curr_middle == 1) and (curr_right == 0):
                robot.scherprechts()
                print "scherprechts"
            elif (curr_left == 0) and (curr_middle == 0) and (curr_right == 0):
                #stop = True
                kruispunt(route)
                print "stop"
            else:
                robot.rechtdoor()

    sleep(.2)


GPIO.cleanup()
