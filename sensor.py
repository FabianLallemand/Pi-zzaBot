import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

leftIR = 14
middleIR = 15
rightIR = 18

class Sensor:

    def setupsensor():

        print "setting up a sensor"
        GPIO.setup(leftIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        GPIO.setup(middleIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        GPIO.setup(rightIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)

        GPIO.setup(leftIR,GPIO.IN) #GPIO 14 -> Left IR out
        GPIO.setup(middleIR,GPIO.IN) #GPIO 15 -> middle IR out
        GPIO.setup(rightIR,GPIO.IN) #GPIO 18 -> Right IR out
