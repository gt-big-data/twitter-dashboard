var socket = io('http://localhost:5000');
var map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -34.397, lng: 150.644},
          zoom: 1
        });

var markers = [];

setInterval(function() {
  var now = new Date();
  markers = markers.filter(function(m) {
    var diff = now.getTime() - m.time.getTime() > 60 * 1000;
    if (diff) {
      m.setMap(null);
    }
    return diff;
  });
}, 10000);

socket.on('connect', function () {
   console.log('connected!');
});

socket.on('coordinates', function(data) {
  console.log(data);
  var coords = getCoordinates(data.data);
  if (!coords) {
    return;
  }

  var marker = new google.maps.Marker({
         position: coords,
         map: map,
         title: 'Hello World!'
       });
  marker.time = coords.time;
  markers.push(marker);
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
