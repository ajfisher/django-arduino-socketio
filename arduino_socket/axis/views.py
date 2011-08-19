from django.shortcuts import get_object_or_404, render, redirect
from django_socketio import events

@events.on_message(channel="axis")
def message(request, socket, message):
    message = message[0]
    if message["action"] == "movement":
        ax = message["ax"]
        ay = message["ay"]
        az = message["az"]
        px = message["px"]
        py = message["py"]
        pz = message["pz"]
        
        socket.broadcast({
            "action": "position", 
            "ax": ax, 
            "ay": ay, 
            "az": az,
            "px": px,
            "py": py,
            "pz": pz,
        })

def showaxis (request, template="showaxis.html"):
    context = {}
    return render(request, template, context)
    
def usephone (request, template="usephone.html"):
    context={}
    return render(request, template, context)
