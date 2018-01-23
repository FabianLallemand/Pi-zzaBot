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

robot = Robot()

GPIO.setup(leftIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(middleIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(leftIR,GPIO.IN) #GPIO 14 -> Left IR out
GPIO.setup(middleIR,GPIO.IN) #GPIO 15 -> middle IR out
GPIO.setup(rightIR,GPIO.IN) #GPIO 18 -> Right IR out

while True:

    buttonstate = GPIO.input(buttonPin)
    if (buttonstate == 0):
        print "start"
        started True
        while started:
            buttonstate = GPIO.input(buttonPin)
            curr_left = GPIO.input(leftIR)
            curr_middle = GPIO.input(middleIR)
            curr_right = GPIO.input(rightIR)
            if (buttonstate == 0)
                started = False

            if (curr_left == 1) and (curr_middle == 0) and (curr_right == 1):
                robot.rechtdoor()
            elif (curr_right != 0) and ((curr_left == 0) or ((curr_left == 0) and (curr_middle == 0))):
                robot.linksaf()
            elif (curr_left != 0) and ((curr_right == 0) or ((curr_right == 0) and (curr_middle == 0))):
                robot.rechtsaf()
            elif (curr_left == 0 ) and (curr_middle == 0) and (curr_right == 0):
                print "stopfunctie"
            else:
                robot.rechtdoor()

    sleep(.2)


GPIO.cleanup()
