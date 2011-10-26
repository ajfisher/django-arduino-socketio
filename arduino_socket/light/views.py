import serial

from settings import *

from django.shortcuts import get_object_or_404, render, redirect
from django_socketio import events


try:
    ser = serial.Serial(SERIAL_INTERFACE, SERIAL_BAUD, timeout=60)
except:
    print "Can't get a serial connection"


@events.on_message(channel="^light")
def message(request, socket, message):
    #import pdb; pdb.set_trace()
    message = message[0]
    if message["action"] == "movement":
        socket.send({"action": "ack"})
        
        # pick up the values from the socket message
        x = int(message["x"])
        y = int(message["y"])
        z = int(message["z"])
        
        # now normalise the values as needed
        if message["method"] == "orientation":
            # put the vals back into +ive integer range as needed
            x += 90 #normalise 0-180
            y += 360 # normalise 0-360
            
        if x > 180:
            x = 180
        if y > 360:
            y = 360
        if z >= 360:
            z = 0

        # work out the y bytes
        # leaving this like this even though it's normalised back to 180 deg.
        # just in case there's any more changes to firefox.
        yh = y >> 8
        if y > 255:
            yl = y - 256
        else:
            yl = y
        # work out the z bytes
        zh = z >> 8
        if z > 255 :
            zl = z - 256
        else:
            zl = z

        print "x: %s y: %s z: %s" % (x, y, z)
        try:
            ser.write("%s%s%s%s%s%s%s" % (chr(255), chr(255), chr(x), chr(yh), chr(yl), chr(zh), chr(zl)))
        except:
            #do  nothing - this is a good test anyway.
            print "Doing nothing as no serial connection: %s" % SERIAL_INTERFACE
        
    elif message["action"] == "test":
        # this is a test of the socket
        print "Test of the socket"
        socket.send({"action": "bcast", "message": "got a test"})


def home (request, template="index.html"):
    context = {}
    return render(request, template, context)

    
def light (request, template="light.html"):
    context = {}
    return render(request, template, context)
    
