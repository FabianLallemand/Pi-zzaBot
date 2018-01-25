import RPi.GPIO as GPIO
from time import sleep
from threading import Thread

linkslamp = 21
rechtslamp = 16
discolamp = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(linkslamp,GPIO.OUT) #linker lichten
GPIO.setup(discolamp,GPIO.OUT) #worden de disco's
GPIO.setup(rechtslamp,GPIO.OUT) #rechter lichten

def discolight(): # Deze def zorgt ervoor dat aan het einde van de rit de disco lampjes aan gaan.
    print("PIZZA IS HERE, LETS GET THIS PARTY STARTED")
    GPIO.output(discolamp,True)
    knipper_rechts()
    knipper_links()
    sleep(10)
    GPIO.output(discolamp,False)

def knipper_links():    # Deze def zorgt ervoor dat de linker lampjes gaan knipperen.


    steps = 0
    while steps < 4:
        GPIO.output(linkslamp,False)
        sleep(0.3)
        GPIO.output(linkslamp,True)
        sleep(0.3)
        steps += 1


def knipper_rechts():    # Deze def zorgt ervoor dat de rechter lampjes gaan knipperen.

    steps = 0
    while steps < 4:
        GPIO.output(rechtslamp,False)
        sleep(0.3)
        GPIO.output(rechtslamp,True)
        sleep(0.3)
        steps += 1
