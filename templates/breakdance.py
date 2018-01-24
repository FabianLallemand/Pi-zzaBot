import RPi.GPIO as GPIO
from time import sleep
from robot_class import Robot

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

robot = Robot()
buttonPin = 26
buttonstate = 1
started = False
run = True

GPIO.setup(21,GPIO.OUT) #linker lichten
GPIO.setup(20,GPIO.OUT) #worden de disco's
GPIO.setup(16,GPIO.OUT) #rechter lichten

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(buttonPin, GPIO.RISING)

while run:
    buttonstate = GPIO.input(buttonPin)
    if (buttonstate == 0):
        print "start"
        started = True
        while started:
            for x in range (0, 1000):
                robot.scherprechts() #links vooruit, rechts achteruit
                GPIO.output(16,True) #rechts ook vooruit
                GPIO.output(21,False)
            for x in range (0, 1000):
                robot.linksaf() #links stil, rechts vooruit
                GPIO.output(21,True) #rechts achteruit
                GPIO.output(16,False)
            for x in range (0, 1000):
                robot.scherplinks() #links achteruit, rechts vooruit
                GPIO.output(16,True) #rechts achteruit
                GPIO.output(21,False)
            for x in range (0, 1000):
                robot.rechtsaf() #links vooruit, rechts stil
                GPIO.output(21,True) #rechts vooruit, linksstil
                GPIO.output(16,False)
            if(GPIO.event_detected(buttonPin)):
                started = False


GPIO.cleanup()
