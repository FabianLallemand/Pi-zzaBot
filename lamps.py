import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT) #links
GPIO.setup(16,GPIO.OUT) #rechst

def discolight(finish):
    if finish == True:
        GPIO.output(20,True)
        sleep(5)
        GPIO.output(20,False)
        print("joepie")
    else:
        print("nog niet klaar of onbekend")

finish = True
discolight(finish)
finish = False
discolight(finish)
