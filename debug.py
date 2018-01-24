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
route = 1
kruisingCount = 0

MotorR1 = 2
MotorR2 = 3
MotorR3 = 4
MotorR4 = 17

MotorL1 = 27
MotorL2 = 22
MotorL3 = 10
MotorL4 = 9

robot = Robot()

GPIO.setup(leftIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(middleIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(MotorR1,GPIO.OUT) #GPIO 2  -> Motor rechts A
GPIO.setup(MotorR2,GPIO.OUT) #GPIO 3  -> Motor rechts B
GPIO.setup(MotorR3,GPIO.OUT) #GPIO 4  -> Motor rechts C
GPIO.setup(MotorR4,GPIO.OUT) #GPIO 17 -> Motor rechts D

GPIO.setup(MotorL1,GPIO.OUT) #GPIO 27 -> Motor Left A
GPIO.setup(MotorL2,GPIO.OUT) #GPIO 22 -> Motor Left B
GPIO.setup(MotorL3,GPIO.OUT) #GPIO 10 -> Motor Left C
GPIO.setup(MotorL4,GPIO.OUT) #GPIO 9  -> Motor Left D

GPIO.setup(21,GPIO.OUT) #linker lichten
GPIO.setup(20,GPIO.OUT) #worden de disco's
GPIO.setup(16,GPIO.OUT) #rechter lichten

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(leftIR,GPIO.IN) #GPIO 14 -> Left IR out
GPIO.setup(middleIR,GPIO.IN) #GPIO 15 -> middle IR out
GPIO.setup(rightIR,GPIO.IN) #GPIO 18 -> Right IR out

def rechtdoor(self):
    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,1)

    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,1)
    sleep(.0008)
    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,1)
    GPIO.output(MotorR4,1)

    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,1)
    GPIO.output(MotorL4,1)
    sleep(.0008)
    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,1)
    GPIO.output(MotorR4,0)

    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,1)
    GPIO.output(MotorL4,0)
    sleep(.0008)
    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,1)
    GPIO.output(MotorR3,1)
    GPIO.output(MotorR4,0)

    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,1)
    GPIO.output(MotorL3,1)
    GPIO.output(MotorL4,0)
    sleep(.0008)
    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,1)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,0)

    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,1)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,0)
    sleep(.0008)
    GPIO.output(MotorR1,1)
    GPIO.output(MotorR2,1)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,0)

    GPIO.output(MotorL1,1)
    GPIO.output(MotorL2,1)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,0)
    sleep(.0008)
    GPIO.output(MotorR1,1)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,0)

    GPIO.output(MotorL1,1)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,0)
    sleep(.0008)
    GPIO.output(MotorR1,1)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,1)

    GPIO.output(MotorL1,1)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,1)
    sleep(.0008)
def linksaf(self):
    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,1)

    sleep(.0008)
    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,1)
    GPIO.output(MotorR4,1)

    sleep(.0008)
    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,1)
    GPIO.output(MotorR4,0)

    sleep(.0008)
    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,1)
    GPIO.output(MotorR3,1)
    GPIO.output(MotorR4,0)

    sleep(.0008)
    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,1)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,0)

    sleep(.0008)
    GPIO.output(MotorR1,1)
    GPIO.output(MotorR2,1)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,0)

    sleep(.0008)
    GPIO.output(MotorR1,1)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,0)

    sleep(.0008)
    GPIO.output(MotorR1,1)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,1)

    sleep(.0008)
def rechtsaf(self):
    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,1)

    sleep(.0008)
    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,1)
    GPIO.output(MotorL4,1)

    sleep(.0008)
    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,1)
    GPIO.output(MotorL4,0)

    sleep(.0008)
    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,1)
    GPIO.output(MotorL3,1)
    GPIO.output(MotorL4,0)

    sleep(.0008)
    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,1)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,0)

    sleep(.0008)
    GPIO.output(MotorL1,1)
    GPIO.output(MotorL2,1)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,0)

    sleep(.0008)
    GPIO.output(MotorL1,1)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,0)

    sleep(.0008)
    GPIO.output(MotorL1,1)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,1)

    sleep(.0008)
def scherplinks(self):
    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,1)

    GPIO.output(MotorL1,1)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,0)
    sleep(.0008)
    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,1)
    GPIO.output(MotorR4,1)

    GPIO.output(MotorL1,1)
    GPIO.output(MotorL2,1)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,0)
    sleep(.0008)
    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,1)
    GPIO.output(MotorR4,0)

    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,1)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,0)
    sleep(.0008)
    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,1)
    GPIO.output(MotorR3,1)
    GPIO.output(MotorR4,0)

    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,1)
    GPIO.output(MotorL3,1)
    GPIO.output(MotorL4,0)
    sleep(.0008)
    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,1)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,0)

    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,1)
    GPIO.output(MotorL4,0)
    sleep(.0008)
    GPIO.output(MotorR1,1)
    GPIO.output(MotorR2,1)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,0)

    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,1)
    GPIO.output(MotorL4,1)
    sleep(.0008)
    GPIO.output(MotorR1,1)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,0)

    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,1)
    sleep(.0008)
    GPIO.output(MotorR1,1)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,1)

    GPIO.output(MotorL1,1)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,1)
    sleep(.0008)
def scherprechts(self):
    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,1)

    GPIO.output(MotorR1,1)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,0)
    sleep(.0008)
    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,1)
    GPIO.output(MotorL4,1)

    GPIO.output(MotorR1,1)
    GPIO.output(MotorR2,1)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,0)
    sleep(.0008)
    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,1)
    GPIO.output(MotorL4,0)

    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,1)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,0)
    sleep(.0008)
    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,1)
    GPIO.output(MotorL3,1)
    GPIO.output(MotorL4,0)

    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,1)
    GPIO.output(MotorR3,1)
    GPIO.output(MotorR4,0)
    sleep(.0008)
    GPIO.output(MotorL1,0)
    GPIO.output(MotorL2,1)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,0)

    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,1)
    GPIO.output(MotorR4,0)
    sleep(.0008)
    GPIO.output(MotorL1,1)
    GPIO.output(MotorL2,1)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,0)

    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,1)
    GPIO.output(MotorR4,1)
    sleep(.0008)
    GPIO.output(MotorL1,1)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,0)

    GPIO.output(MotorR1,0)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,1)
    sleep(.0008)
    GPIO.output(MotorL1,1)
    GPIO.output(MotorL2,0)
    GPIO.output(MotorL3,0)
    GPIO.output(MotorL4,1)

    GPIO.output(MotorR1,1)
    GPIO.output(MotorR2,0)
    GPIO.output(MotorR3,0)
    GPIO.output(MotorR4,1)
    sleep(.0008)

while not stop:
    GPIO.output(21,True)
    GPIO.output(16,True)
    while True:
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
        else:
            robot.rechtdoor()
            print "rechtdoor"
    sleep(.2)


GPIO.cleanup()
