import RPi.GPIO as GPIO
from time import sleep
from robot_class import Robot

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

robot = Robot()
buttonPin = 26
buttonstate = 1
started = False

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    buttonstate = GPIO.input(buttonPin)
    if (buttonstate == 0):
        print "start"
        started = True
        while started:
            for x in range (0, 500):
                robot.scherprechts()
            for x in range (0, 250):
                robot.linksaf()
            for x in range (0, 500):
                robot.scherplinks()
            for x in range (0, 250):
                robot.rechtsaf()

GPIO.cleanup()
