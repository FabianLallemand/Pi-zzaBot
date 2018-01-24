# imports are program code that is needed to run your program
from flask import Flask, render_template # to run Flask
import datetime
import os # needed to check if events file exists

'''
Source file: flask_show_events_v1.py

Start: sudo flask_show_events_v1.py

(v1) This code starts a Flask webserver. The user can request a web page from this web server.
The web server will show the home page with the current system time

(v2) Now the web server can show a page with button events

Input:
- Browser requests
Output:
- A home web page
- A page with button events

 (v3) Number of events is shown on webpage

@author: Koen Warner
@version:  v1.1,  07 okt. 2014
(c) 2014 Koen Warner

'''


# create a Flask objec called app
app = Flask(__name__)

# run the code below when someone accesses the root URL of the server: http://<IP address of Flask server:port
# For example: http://172.16.0.0:8085/
@app.route("/")
def home():
	# get current time and store it in variable now
	now = datetime.datetime.now()
	# create formatted string using the date and time from the now object
	timeString = now.strftime("%Y-%m-%d %H:%M")
	# Create a (Python) dictionary of variables; this will be passed into the html template
	templateData = {
		'title' : "Button Events",
		'time' : timeString
	}
	# return the main.html template to the web browser and pass into it the variables in the templateData dictionary
	return render_template('index.php', **templateData)

# run the code below when someone accesses the /readevents URL of the server
# For example: http://172.16.0.0:8085/readevents
@app.route("/readevents")
def read_events():
	response = "OK" # whether things run OK or not
	lines = 0 # Python list

	# get current time and store it in variable now
	now = datetime.datetime.now()
	# create formatted string using the date and time from the now object
	timeString = now.strftime("%Y-%m-%d %H:%M")

	try:
		# the button events file
		file_name = "events.txt"

		# check if event file already exists; if not, create it
		if not os.path.exists(file_name):
			response = "Event file does not exist"
		else:
			# open the button events event file for reading
			event_file = open(file_name, "r")
			# read all lines from the file into a Python list called 'lines'
			lines = [line.rstrip('\n') for line in event_file]	# strip new line character from each line in file
			# close event file
			event_file.close()


	except:
		response = "There was an error reading the events "

	# create a (Python) dictionary of variables; this will be passed into the readevents.html template
	templateData = {
		'title' : "Button Events",
		'greetings' : "Whether is the button is pressed or released",
		'lines' : lines, # this is the Python list which contains the events
		'time' : timeString, # the time stamp we created before
		'response' : response # all OK, or did something go wrong
	}

	return render_template('readevents.html', **templateData)



# if the script was run directly from the command line
if __name__ == "__main__":
	# have the local host server listen on port 80, and report any errors
	app.run(host='0.0.0.0', port=8085, debug=True) # if permission denied; change port
