Introduction
============

django-arduino-socketio is a BSD Licensed set of applications that utilises web sockets to interact with an Arduino microcontroller.

This project was inspired by the awesome django-socketio library built by Stephen McDonald as it has given me the opportunity to combine both of my interests - Django and Arduino together via a web application.

Installation
=============

You'll need the following dependencies (please see individual installation process for each project):

    * An arduino microcontroller
    * Django
    * django-socketio
    
Assuming you have all of these set up, you can download and extract these project files to a directory or else just grab the latest from github::

    $ git git://github.com/ajfisher/django-arduino-socketio.git
    
Mobile
------

You'll need an iOS device that's relatively new or else an android device running Firefox (note that Honeycomb tablets will work just using the standard android browser and I'm assuming all ICS browsers will work fine). Any of these can interact with the Device Orientation API so you can get sensor data from them.    

General usage
=====

Django
------

You need to run the django socketio server. Please see django docs and django-socketio for specifics but here's the gist::

    $ python manage.py runserver_socketio addr:port
    
You'll then be able to browse to addr:port via your web browser of choice and you should see the server up and running. From the home page at / you'll be able to follow the demos and interactions.

Local Settings
..............

To make it easy to configure, you can edit the local_settings.py folder in the root. Each of the config settings is explained in the file and it should be pretty straight forward to change (it's just serial device paths etc).

Mobile tests
------------

The basic tests are simply there to establish whether you can get the server running, your device works with the deviceapi and you can stream data to the server using web sockets. You should view these as tests to ensure the core system works as other wise debugging will be a lot harder.

Demos
=================

Light Interaction
-----------------

This demo maps the three device axes using the device orientation event to an RGB LED such that each colour is controlled by each of the axes. Build the demo circuit, load the sketch then try the example from your phone and make some pretty colours.


Arduino + Circuit
------------------

Circuit can be seen in the light_interaction_serial/circuit.fz as a fritzing file or in light_interaction_serial/schematic.png as a simple schematic. This uses a common anode RGB LED to show the tilt of the various light sources so wire it up::

    R = Pin 3
    G = Pin 5
    B = Pin 6

Don't forget resistors for each colour channel

Load the arduino with the light_interaction_serial.pde

Django
------

Run the django server as per the instructions above. Make sure SERIAL_INTERFACE and SERIAL_BAUD are set to what your arduino is using in local_settings.py or you won't see anything happen.

Mobile
------

Point your web browser at the IP address and start moving your phone around. From there you'll see the colour of the various R, G and B LEDs start to change in response to the tilt.

Notes
-----

You may flood your network with this, I tend to run my server on a wired network port so as to keep the mobile space free as you'll be sending a lot of data very quickly.

TODO:
=====

* Do a light interaction using krohling's arduino web sockets client to have full web sockets stack
* Show a demo with both orientation events and web interface events on some servos etc.


