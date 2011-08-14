var socket;
var room = "puppet";

// use this for Firefox
window.addEventListener("MozOrientation", update_accelerometer, true);

// Mobile Safari
//window.addEventListener("devicemotion", update_accelerometer, true);


function update_accelerometer(e){
    // gets the accelerometer vals and passes them back
	if(!!e.x) {
		// Firefox
		var x = e.x*90;
		var y = e.y*90;
		var z = 0;
		update_text(x, y, z); // no compass value for Firefox :( you can get z accel though
		socket.send({room: room, action: 'movement', x: x, y: y, z: z});
		
	} else if (!!e.accelerationIncludingGravity){
		// Mobile Safari
		update_text(e.gamma, e.beta, e.alpha);	
	} else {
		//alert("you don't really support devicemotion, do you?");
		;
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
	});
	
	// this is the browser test version
	$(window).bind("mousemove", function(e) {
		var x = e.pageX;
		var y = e.pageY;
		socket.send({room: room, action: 'movement', x: x, y: y, z: 0});
		update_text(x, y, 0);
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
