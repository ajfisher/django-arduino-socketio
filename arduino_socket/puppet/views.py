from django.shortcuts import get_object_or_404, render, redirect
from django_socketio import events

@events.on_message(channel="^puppet")
def message(request, socket, message):
    message = message[0]
    if message["action"] == "movement":
        print "x: %s y: %s z: %s" % (message["x"], message["y"], message["z"])
        socket.send({"action": "ack"})
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
    
