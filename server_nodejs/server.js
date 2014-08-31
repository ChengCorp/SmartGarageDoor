var http = require('http');
var url = require('url');

var handlePost = function (request, response) {
	if (request.url == "/") {
		var parsedUrl = url.parse(request.url, true);
		
	}
}

var handleGet = function (request, response) {
	if (request.url == "/") {
		
	} else if (request.url == "/test") {
		response.writeHead(200, { 'content-type': 'text/plain' });
		response.write("I am alive.");
		response.end();
	} else {
		response.writeHead(200, { 'content-type': 'text/plain' });
		response.write("Wrong directory");
		response.end();
		console.log(request.url);
	}
}

	
	
var server = http.createServer(function (request, response) {
	if (request.method == 'POST') {
		handlePost();
	} else if (request.method == 'GET') {
		handleGet();
	}
});
server.listen(3639);
console.log("Listening on port 3639");