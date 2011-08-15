Introduction
============

django-arduino-socketio is a BSD Licensed set of applications that utilises web sockets to interact with an Arduino microcontroller.

This project was inspired by the awesome django-socketio library built by Stephen McDonald as it has given me the opportunity to combine both of my interests - Django and Arduino together via a web application.

Installation
=============

You'll need the following dependencies (please see individual installation for each project):

    * An arduino microcontroller
    * Django
    * django-socketio
    
Assuming you have all of these set up, you can download and extract these project files to a directory or else just grab the latest from github::

    $ git git://github.com/ajfisher/django-arduino-socketio.git
    
Usage
=====

Django
------

You need to run the django socketio server. Please see django docs and django-socketio for specifics but here's the gist::

    $ python manage.py runserver_socketio addr:port
    
You'll then be able to browse to addr:port via your web browser of choice and you should see the server up and running. If you take various actions you'll be able to see the socket messages going through in the log.

Arduino
--------

Install the socket_interaction.pde file as per normal. This uses a common anode RGB LED to show the tilt of the various light sources so wire it up::

    R = IN 3
    G = Pin 5
    B = Pin 6

If you watch the serial output then you can see the data coming in from the python server.

Mobile
------

You'll need an iOS device that's relatively new or else an android device running Firefox. Either of these can interact with the Device Orientation API so you can get sensor data from them.

Point your web browser at the IP address and start moving your phone around. From there you'll see the colour of the various R, G and B LEDs start to change in response to the tilt.
