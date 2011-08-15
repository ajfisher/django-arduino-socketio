var socket;
var room = "puppet";
var z = 250;  // use this as a dummy for FF

// use this for Firefox
window.addEventListener("MozOrientation", update_accelerometer, true);

// Mobile Safari
window.addEventListener("devicemotion", update_accelerometer, true);


function update_accelerometer(e){
    // gets the accelerometer vals and passes them back
	if(!!e.x) {
		// Firefox
		var x = Math.round(e.x*90);
		var y = Math.round(e.y*90);
		//var z = 0;
		update_text(x, y, z); // no compass value for Firefox :( you can get z accel though
		socket.send({room: room, action: 'movement', x: x, y: y, z: z, method: 'orientation'});
		
	} else if (!!e.accelerationIncludingGravity){
		// Mobile Safari
		var x = Math.round(e.gamma);
		var y = Math.round(e.beta);
		z = Math.round(e.alpha);
		update_text(x, y, z);
		socket.send({room: room, action: 'movement', x: x, y: y, z: z, method: 'orientation'});
		
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
