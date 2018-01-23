import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

i=0

leftIR = 14
middleIR = 15
rightIR = 18

GPIO.setup(leftIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(middleIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)

MotorR1 = 2
MotorR2 = 3
MotorR3 = 4
MotorR4 = 17

MotorL1 = 27
MotorL2 = 22
MotorL3 = 10
MotorL4 = 9

GPIO.setup(leftIR,GPIO.IN) #GPIO 14 -> Left IR out
GPIO.setup(middleIR,GPIO.IN) #GPIO 15 -> middle IR out
GPIO.setup(rightIR,GPIO.IN) #GPIO 18 -> Right IR out

GPIO.setup(MotorR1,GPIO.OUT) #GPIO 2  -> Motor rechts A
GPIO.setup(MotorR2,GPIO.OUT) #GPIO 3  -> Motor rechts B
GPIO.setup(MotorR3,GPIO.OUT) #GPIO 4  -> Motor rechts C
GPIO.setup(MotorR4,GPIO.OUT) #GPIO 17 -> Motor rechts D

GPIO.setup(MotorL1,GPIO.OUT) #GPIO 27 -> Motor Left A
GPIO.setup(MotorL2,GPIO.OUT) #GPIO 22 -> Motor Left B
GPIO.setup(MotorL3,GPIO.OUT) #GPIO 10 -> Motor Left C
GPIO.setup(MotorL4,GPIO.OUT) #GPIO 9  -> Motor Left D

leftstate = 0
middlestate = 0
rightstate = 0
print leftstate
print middlestate
print rightstate

print GPIO.input(leftIR)
print GPIO.input(middleIR)
print GPIO.input(rightIR)

while True:
    curr_left = GPIO.input(leftIR)
    curr_middle = GPIO.input(middleIR)
    curr_right = GPIO.input(rightIR)

    if (curr_right == 0) or ((curr_right == 0) and (curr_middle == 0)):
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


    elif (curr_left == 0) or ((curr_left == 0) and (curr_middle == 0)):
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
    elif (curr_left == 0) and (curr_right == 0) and (curr_middle == 0):
        print "kruispunt"
        GPIO.output(MotorR1,0)
        GPIO.output(MotorR2,0)
        GPIO.output(MotorR3,0)
        GPIO.output(MotorR4,0)

        GPIO.output(MotorL1,0)
        GPIO.output(MotorL2,0)
        GPIO.output(MotorL3,0)
        GPIO.output(MotorL4,0)
    else:
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


GPIO.cleanup()
