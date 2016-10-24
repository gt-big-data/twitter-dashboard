var socket = io('http://localhost:5000');
 socket.on('connect', function () {
   console.log('connected!');
   socket.emit('hello', { message: 'hello world' });
 });

 socket.on('goodbye', function(message) {
   console.log(message);
 });
