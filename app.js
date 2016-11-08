var socket = io('http://localhost:5000');
var map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -34.397, lng: 150.644},
          zoom: 1
        });

socket.on('connect', function () {
   console.log('connected!');
});

socket.on('coordinates', function(data) {
  var coords = getCoordinates(data.data);
  if (!coords) {
    return;
  }

  var circle = new google.maps.Circle({
    map: map,
    center: coords,
    radius: 1000,
  });
  circle.time = coords.time;
  circle.data = data.data;
  setTimeout(function() {
    circle.setMap(null);
  }, 5000);
});

socket.on('trending', function(data) {
  // console.log(data)
});

function getCoordinates(tweet) {
  if (!tweet.place){
    return false;
  }
  var bb = tweet.place.bounding_box.coordinates[0];
  function reducer(x, y) {
    return x + y;
  }
  var lat = bb.map(function(x) {
    return x[0];
  }).reduce(reducer) / bb.length;
  var lng = bb.map(function(x) {
    return x[1];
  }).reduce(reducer) / bb.length;
  return {
    lat: lng,
    lng: lat,
    time: new Date()
  };
}
