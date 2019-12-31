const http = require('http');
const fs   = require('fs');
var response;
var request;

var server = http.createServer(getFromClient);


server.listen(8080);
console.log('start!');

function getFromClient(req,res){
    request = req;
    response = res;
    fs.readFile('./2_2_2.htm', 'UTF-8', writeToResponse);
    console.log("200 OK");
    console.log("----------");

}

function writeToResponse(error, data) {
    var content = data;
    content = content.replace(/dummy_title/g, 'This is title');
    content = content.replace(/dummy_contents/g, 'This is contents');
    response.writeHead(200, {'Content-Type': 'text/html'});
    response.write(content);
    response.end();
}