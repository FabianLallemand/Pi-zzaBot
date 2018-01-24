import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT) #linker lichten
GPIO.setup(20,GPIO.OUT) #worden de disco's
GPIO.setup(16,GPIO.OUT) #rechter lichten
GPIO.setup(26,GPIO.OUT)

buttonPin = 26
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


buttonstate = 1
stop = False


while not stop:

    buttonstate = GPIO.input(buttonPin)
    if (buttonstate == 0):
        print "start"
        started = True
        while started:
            GPIO.output(21,True)
            GPIO.output(16,True)
            GPIO.output(20, True)
            sleep(5)
            GPIO.output(21,False)
            GPIO.output(20,False)
            GPIO.output(16,False)
            buttonstate = 1

GPIO.cleanup
