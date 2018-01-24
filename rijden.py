import RPi.GPIO as GPIO
from time import sleep
from robot_class import Robot
from lamps import *
from threading import Thread
from flask import Flask, render_template, request, url_for, redirect
import datetime
import os
import cgi

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

leftIR = 14
middleIR = 15
rightIR = 18

buttonPin = 26
buttonstate = 1
started = False
stop = False
kruisingCount = 0
#route = 3

form = cgi.FieldStorage()
route = form.getvalue('route')

robot = Robot()
app = Flask(__name__)

@app.route("/")
def home():
	now = datetime.datetime.now()
	timeString = now.strftime("%Y-%m-%d %H:%M")
	templateData = {
		'title' : "Button Events",
		'time' : timeString
	}
	return render_template('index.php', **templateData)

@app.route('/rijden', methods=['GET', 'POST'])
def rijden():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home'))

    # show the form, it wasn't submitted
    return render_template('rijden.py')

if __name__ == "__main__":
	# have the local host server listen on port 80, and report any errors
    app.run(host='0.0.0.0', port=8085, debug=True)



print(route)

def kruispunt(route):
    if (route == 1):
        knipper_links()
        for x in range(0, 150):
            robot.linksaf()
        while (GPIO.input(middleIR)):
            robot.scherplinks()
    elif (route == 2):
        sleep(2)
        robot.rechtdoor()
    elif (route == 3):
        knipper_rechts()
        for x in range(0, 150):
            robot.rechtsaf()
        while (GPIO.input(middleIR)):
            robot.scherprechts()
    else:
        print("no route to host")

GPIO.setup(leftIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(middleIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightIR,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(21,GPIO.OUT) #linker lichten
GPIO.setup(20,GPIO.OUT) #worden de disco's
GPIO.setup(16,GPIO.OUT) #rechter lichten

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(leftIR,GPIO.IN) #GPIO 14 -> Left IR out
GPIO.setup(middleIR,GPIO.IN) #GPIO 15 -> middle IR out
GPIO.setup(rightIR,GPIO.IN) #GPIO 18 -> Right IR out

while not stop:

    buttonstate = GPIO.input(buttonPin)
    if (buttonstate == 0):
        print("start")
        started = True
        GPIO.output(21,True)
        GPIO.output(16,True)
        GPIO.output(20, True)
        while started:
            buttonstate = GPIO.input(buttonPin)
            curr_left = GPIO.input(leftIR)
            curr_middle = GPIO.input(middleIR)
            curr_right = GPIO.input(rightIR)

            if (curr_left == 0) and (curr_middle == 0) and (curr_right == 1):
                robot.linksaf()
                print("linksaf")
            elif (curr_left == 1) and (curr_middle == 0) and (curr_right == 0):
                robot.rechtsaf()
                print("rechtsaf")
            elif (curr_left == 0) and (curr_middle == 1) and (curr_right == 1):
                robot.scherplinks()
                print("scherplinks")
            elif (curr_left == 1) and (curr_middle == 1) and (curr_right == 0):
                robot.scherprechts()
                print("scherprechts")
            elif (curr_left == 0) and (curr_middle == 0) and (curr_right == 0):
                if (kruisingCount == 1):
                    started = False
                    stop = True
                else:
                    kruispunt(route)
                    kruisingCount += 1
            else:
                robot.rechtdoor()

    sleep(.2)


GPIO.cleanup()
