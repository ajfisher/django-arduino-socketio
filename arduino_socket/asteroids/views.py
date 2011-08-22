from django.shortcuts import get_object_or_404, render, redirect
from django_socketio import events

@events.on_message(channel="asteroids")
def message(request, socket, message):
    message = message[0]
    if message["action"] == "movement":     
        # pick up the values from the socket message
        ax = message["ax"]
        ay = message["ay"]
        
        socket.broadcast({"action": "player_state", "ax": ax, "ay": ay, })



def phonecontrol (request, template="asteroids_phone.html"):
    context = {}
    return render(request, template, context)
    
def showgame (request, template="asteroids_play.html"):
    context = {}
    return render(request, template, context)
