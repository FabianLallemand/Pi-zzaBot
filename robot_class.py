import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

MotorR1 = 2
MotorR2 = 3
MotorR3 = 4
MotorR4 = 17

MotorL1 = 27
MotorL2 = 22
MotorL3 = 10
MotorL4 = 9

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

class Robot:
    GPIO.setup(MotorR1,GPIO.OUT) #GPIO 2  -> Motor rechts A
    GPIO.setup(MotorR2,GPIO.OUT) #GPIO 3  -> Motor rechts B
    GPIO.setup(MotorR3,GPIO.OUT) #GPIO 4  -> Motor rechts C
    GPIO.setup(MotorR4,GPIO.OUT) #GPIO 17 -> Motor rechts D

    GPIO.setup(MotorL1,GPIO.OUT) #GPIO 27 -> Motor Left A
    GPIO.setup(MotorL2,GPIO.OUT) #GPIO 22 -> Motor Left B
    GPIO.setup(MotorL3,GPIO.OUT) #GPIO 10 -> Motor Left C
    GPIO.setup(MotorL4,GPIO.OUT) #GPIO 9  -> Motor Left D

    def rechtdoor(self):
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,1)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,1)
        sleep(.001)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,1)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,1)
        sleep(.001)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,0)
        sleep(.001)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,0)
        sleep(.001)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)
        sleep(.001)
        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)
        sleep(.001)
        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)
        sleep(.001)
        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,1)

        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,1)
        sleep(.001)
    def linksaf(self):
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,1)

        sleep(.001)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,1)

        sleep(.001)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,0)

        sleep(.001)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,0)

        sleep(.001)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        sleep(.001)
        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        sleep(.001)
        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        sleep(.001)
        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,1)

        sleep(.001)
    def rechtsaf(self):
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,1)

        sleep(.001)
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,1)

        sleep(.001)
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,0)

        sleep(.001)
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,0)

        sleep(.001)
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)

        sleep(.001)
        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)

        sleep(.001)
        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)

        sleep(.001)
        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,1)

        sleep(.001)
    def scherplinks(self):
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,1)

        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)
        sleep(.001)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,1)

        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)
        sleep(.001)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)
        sleep(.001)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,0)
        sleep(.001)
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,0)
        sleep(.001)
        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,1)
        sleep(.001)
        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,1)
        sleep(.001)
        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,1)

        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,1)
        sleep(.001)
    def scherprechts(self):
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,1)

        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)
        sleep(.001)
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,1)

        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)
        sleep(.001)
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,0)

        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)
        sleep(.001)
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,1)
        GPIO.output(MotorL4,0)

        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,1)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,0)
        sleep(.001)
        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)

        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,0)
        sleep(.001)
        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,1)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)

        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,1)
        GPIO.output(MotorR4,1)
        sleep(.001)
        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)

        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,1)
        sleep(.001)
        GPIO.output(MotorL1,1)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,1)

        GPIO.output(MotorR1,1)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,1)
        sleep(.001)
