import RPi.GPIO as GPIO
from time import sleep
from threading import Thread

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT) #linker lichten
GPIO.setup(21,GPIO.OUT) #worden de disco's
GPIO.setup(16,GPIO.OUT) #rechter lichten


def discolight(finish):
    if finish == True:
        GPIO.output(21,True)
        sleep(5)
        GPIO.output(21,False)
        print("joepie")
    else:
        print("nog niet klaar of onbekend")


def knipper_links():
    steps = 0
    while steps < 9:
        GPIO.output(20,False)
        sleep(0.3)
        GPIO.output(20,True)
        sleep(0.3)
        steps += 1


def knipper_rechts():
    steps = 0
    while steps < 9:
        GPIO.output(16,False)
        sleep(0.3)
        GPIO.output(16,True)
        sleep(0.3)
        steps += 1


rechtsthread = knipper_rechts()
linksthread = knipper_links()
