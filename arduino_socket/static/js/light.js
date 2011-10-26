var socket;
var room = "light";

var last_sent = (new Date()).getTime();
var threshold = 100; // msec between sends
			
window.addEventListener("deviceorientation", update_gyro, true);

function update_gyro(e) {
	// gets the gyro position
    var x, y, z = 0;
    var o = deviceOrientation(e);
	
	update_text(o.gamma, o.beta, o.alpha);
    if ((new Date()).getTime() - last_sent > threshold) {
		socket.send({room: room, action: 'movement', x: o.gamma, y: o.beta, z: o.alpha, method: 'orientation'});
    }
}
		
function update_text(x, y, z) {
    // updates the text on the screen
    $("#xval").text(x);
    $("#yval").text(y);
    $("#zval").text(z);

}

$(function() {


	var started = false;
	// socket tester.
	$("#test").click (function () {
		socket.send({room: room, action: 'test'});
		z++;
	});
	
	// this is the browser test version
	$(window).bind("mousemove", function(e) {
		var x = e.pageX;
		var y = e.pageY;
		var z = 255;
		socket.send({room: room, action: 'movement', x: x, y: y, z: z, method: 'mouse'});
		update_text(x, y, z);
	});
	
	
	// now we do the mobile version.
	
	socket = new io.Socket();
	socket.connect();
	socket.on('connect', function() {
		socket.subscribe(room);
	});
	
    socket.on('message', function(data) {
        switch (data.action) {
            case 'bcast':
                console.log(data.message)
                //console.log(
                break;
        }
    });


});
