# imports are program code that is needed to run your program
import RPi.GPIO as GPIO  # import library for working with Raspberry's GPIO
import time  # needed to use sleep()
import os  # needed to check if event file already exists
import datetime  # needed to create date time string


'''
Source file: button_events_v5.py

Start: sudo python button_events_v5.py

(v1) This code reads the status of a pin on the Raspberry PI. The pin is attached to a push button. 
The code is constantly polling the pin. When the button is pressed, the code will detect this. A '0' is 
read from the pin. An event is then created: 'pressed'. If the button is released the code will detect 
this too. A '1' is read from the pin and an event 'released' is created. These events are written to console.

(v2) The events are also written to a text file on the Raspberry PI

Each time an event occurs: : 
- add a time stamp to the event
- write event to console
- write event to the event file

(v3) No changes in code
(v4) No changes in code
(v5) Keep track of number of events and show that on console
(v6) No changes in code

Input: Raspberry PI pin state changes
Output:	events to console and file, number of events to console

@author: Koen Warner (koen)
@version:  v1.1,  07 okt. 2014
(c) 2014 Koen Warner


'''

###############################
# Global variables and set up #
###############################

# global variables
number_events = 0 # counting number of events

buttonPin = 23  # this will be an input pin to which the button is attached
				# in this case pin GPIO23 (which is pin number 16)
prev_state = 1  # set start state to 1 (button released)
event_file_name = "events.txt" # file to store events in

# we're using the BCM pin layout; these pin names/numbers are referenced on the cobbler
GPIO.setmode(GPIO.BCM)

# set pin GPIO23 to be an input pin; this pin will read the button state
# activate pull down for pin GPIO23
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)



#############
# Functions #
#############

# Add an event to the event file; before writing to file, add a time stamp to the event
def persist(event):  # an event is 'pressed' or 'released'

	# get current time and store it in variable now
	now = datetime.datetime.now()
	# create formatted string using the date and time from the now object
	# this will be of form: 2014-07-18 19:55:01
	timeString = now.strftime("%Y-%m-%d %H:%M:%S")
	# link event with date-time string
	event = timeString + "->" + event
	# show new event on console
	print event
	# open file for reading
	global event_file_name
	
	# check if event file already exists; if not, create it
	if not os.path.exists(event_file_name):
		open(event_file_name, "w").close()
	
	# open event file for reading
	event_file = open(event_file_name, "a")
	
	# write event to the file
	event_file.write(event + "\n")	# add a carriage return to get events on seperat lines in the file
	
	# Counting number of events 
	global number_events
	# keep count of number of events
	# write number of events up till now to console
	
	# close event file
	event_file.close()



############
# Run code #
############

# Keep on executing this loop forever
event = 1

print "Button Events versie 5"

# keep on executing this loop forever (until someone stops the program)
while True:

	# read the current button state by reading pin GPIO23 on the Raspberry PI
	# the curr_state can be '0' (if button pressed) or '1' (if button released)
	curr_state = GPIO.input(buttonPin)

	# if state changed, take some actions
	if (curr_state != prev_state):  # state changed from '1' to '0' or from '0' to '1'
		if (curr_state == 1):  # button changed from pressed ('0') to released ('1')
			event = "released"
		else:   # button changed from released ('1') to pressed ('0')
			event = "pressed"  # print event to console
		prev_state = curr_state  # store current state

		# store event by using the function persist()
		persist(event)
		
	time.sleep(0.02)  # sleep for a while, to prevent bouncing


# when exiting, reset all pins
GPIO.cleanup()
