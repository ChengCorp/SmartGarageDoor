var http = require('http');
var url = require('url');
var queryString = require( "querystring" );
var fs = require('fs');

var filename = "/data.txt";

var handlePost = function (request, response) {
	if (request.url == "/") {
		var parsedUrl = url.parse(request.url, true);
		
		fs.writeFile(filename, queryUrl.query, function(err) {
			if(err) {
				console.log(err);
			} else {
				console.log("The file was saved!");
			}
		});
	}
}

var handleGet = function (request, response) {
	if (request.url == "/") {
		
		//var queryObj = queryString.parse ( parsedUrl.query );
		
		//var obj = JSON.parse( queryObj.jsonData );
		
		resp.writeHead(200, {"Content-Type":"text/html"});
		fs.readFile(filename, "utf8", function (err, data) {
			if (err) throw err;
			resp.write(data);
			resp.end();
		});
		
	} else if (request.url == "/test") {
		response.writeHead(200, { 'content-type': 'text/plain' });
		response.write("TESTING: I am alive.");
		response.end();
	} else {
		response.writeHead(200, { 'content-type': 'text/plain' });
		response.write("Wrong directory at " + request.url);
		response.end();
		console.log(request.url);
	}
}

	
	
var server = http.createServer(function (request, response) {
	if (request.method == 'POST') {
		handlePost(request, response);
	} else if (request.method == 'GET') {
		handleGet(request, response);
	}
});
server.listen(3639);
console.log("Listening on port 3639");