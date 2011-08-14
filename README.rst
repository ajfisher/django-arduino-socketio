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
    
You'll then be able to browse to addr:port via your web browser of choice and you should see the server up and running.

Arduino
--------

Install the Arduino pde file as per normal.

Mobile
------
