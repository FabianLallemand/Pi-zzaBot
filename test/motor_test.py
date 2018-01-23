import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
i=0

#Motor rechts = motor 1
#IN1 = GPIO2
#IN2 = GPIO3
#IN3 = GPIO4
#IN4 = GPIO17
#
#Motor Links = motor 2
#IN1 = GPIO27
#IN2 = GPIO22
#IN3 = GPIO10
#IN4 = GPIO9

leftIR = 14
middleIR = 15
rightIR = 18

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

print "Turning motor on"
while i!=1000:
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
    i+=1



print "Stopping motor"


GPIO.cleanup()
