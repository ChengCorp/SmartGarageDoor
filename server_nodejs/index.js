var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var bodyParser = require('body-parser');

var fs = require('fs');

var filename = "data.txt";

app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use( bodyParser.urlencoded() ); // to support URL-encoded bodies

app.post('/', function(request, response){
  
  var istream = JSON.stringify(request.body);
  
  fs.writeFile(filename, istream, function(err) {
    if (err) throw err;
    //console.log("The file was saved!");
  });

  response.set('Content-Type', 'text/plain');
  response.send('');
});

app.get('/', function(request, response){
  fs.readFile(filename, "utf8", function (err, data) {
    if (err) throw err;
    response.set('Content-Type', 'text/plain');
    response.send(data);
  });
    
  //response.sendfile('index.html');
});

app.get('/test', function(request, response){
  response.set('Content-Type', 'text/plain');
  response.send('TESTING: I am alive.');
});


io.on('connection', function(socket){
  console.log('a user connected');
  socket.on('disconnect', function(){
    console.log('user disconnected');
  });
  socket.on('chat message', function(msg){
    io.emit('chat message', msg);
  });
});

http.listen(3639, '192.168.0.37', function(){
  console.log('listening on 192.168.0.37:3639');
});