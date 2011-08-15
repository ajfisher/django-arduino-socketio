import serial

from django.shortcuts import get_object_or_404, render, redirect
from django_socketio import events

SERIAL_INTERFACE = "/dev/ttyUSB0"
SERIAL_BAUD = 115200

try:
    ser = serial.Serial(SERIAL_INTERFACE, SERIAL_BAUD, timeout=60)
except:
    print "Can't get a serial connection"


@events.on_message(channel="^puppet")
def message(request, socket, message):
    message = message[0]
    if message["action"] == "movement":
        socket.send({"action": "ack"})
        
        # pick up the values from the socket message
        x = int(message["x"])
        y = int(message["y"])
        z = int(message["z"])
        
        # now normalise the values as needed
        if message["method"] == "orientation":
            # put the vals back into +ive integer range 0-180
            x += 90
            y += 90
            
        if x > 180:
            x = 180
        if y > 180:
            y = 180
        if z >= 360:
            z = 0

        # work out the z bytes
        zh = z >> 8
        if z > 255 :
            zl = z - 256
        else:
            zl = z

        #print "x: %s y: %s z: %s" % (x, y, z)
        ser.write("%s%s%s%s%s%s" % (chr(255), chr(255), chr(x), chr(y), chr(zh), chr(zl)))
        
    elif message["action"] == "test":
        # this is a test of the socket
        print "Test of the socket"
        socket.send({"action": "bcast", "message": "got a test"})


def home (request, template="index.html"):
    context = {"status" : "Booked"}
    return render(request, template, context)
    
def drive (request, template="drive.html"):
    context = {}
    return render(request, template, context)
    