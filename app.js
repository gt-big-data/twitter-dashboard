var socket = io('http://localhost:5000');
var map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -34.397, lng: 150.644},
          zoom: 8
        });

socket.on('connect', function () {
   console.log('connected!');
});

socket.on('coordinates', function(data) {
  console.log(data);
});

socket.on('trending', function(data) {
  // console.log(data)
});
