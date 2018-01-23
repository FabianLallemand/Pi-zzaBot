import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

leftIR = 14
middleIR = 15
rightIR = 18

prev_state = 1

GPIO.setup(leftIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(middleIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:

	curr_state = GPIO.input(middleIR)

	if (curr_state != prev_state):
		if (curr_state == 1):  # button changed from pressed ('0') to released ('1')
			event = "on"
			print event  # print event to console
		else:   # button changed from released ('1') to pressed ('0')
			event = "of"  # print event to console
			print event
		prev_state = curr_state  # store current state

	sleep(0.02)  # sleep for a while, to prevent bouncing

# when exiting, reset all pins
GPIO.cleanup()
