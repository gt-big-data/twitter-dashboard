var socket = io('http://localhost:5000');
socket.on('connect', function () {
   console.log('connected!');
});

socket.on('coordinates', function(data) {
   console.log(data)
});

socket.on('trending', function(data) {
  console.log(data)
});
