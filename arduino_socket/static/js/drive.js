var socket;
var room = "light";
var z = 250;  // use this as a dummy for FF

// use this for Firefox
window.addEventListener("MozOrientation", update_accelerometer, true);

// Mobile Safari
window.addEventListener("devicemotion", update_accelerometer, true);


        function update_accelerometer(e){
            // gets the accelerometer vals and passes them back
            var x, y, z = 0;
            
            // need to do this to normalise Firefox back to spec
	        if(!e.gamma && !e.beta) {
		        // Firefox
		        e.gamma = (e.x * 90);
		        e.beta = (e.y * 180);
		        e.alpha = 0;
		        e.accelerationIncludingGravity = function() {
		        	this.x = 0;
		        	this.y = 0;
		        	this.z = 0;
	        	}
		        e.accelerationIncludingGravity.x = 0;
		        e.accelerationIncludingGravity.y = 0;
		        e.accelerationIncludingGravity.z = e.z;
	        } 

			x = Math.round(e.gamma); // tilt x axis
			y = Math.round(e.beta); // tilt y axis
			//z = Math.round(e.alpha); // tilt z axis (actually compass)
			z=250;
			update_text(x, y, z); // no compass value for Firefox :( you can get z accel though
			socket.send({room: room, action: 'movement', x: x, y: y, z: z, method: 'orientation'});
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
