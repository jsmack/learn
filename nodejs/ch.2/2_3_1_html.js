const http = require('http');
const fs   = require('fs');
const ejs  = require('ejs');

const index_page = fs.readFileSync('./2_3_1.htm', 'UTF-8');
var server = http.createServer(getFromClient);


server.listen(8080);
console.log('start!');

function getFromClient(request, response){
    var content = ejs.render(index_page);
    response.writeHead(200, {'Content-Type': 'text/html'});
    response.write(content);
    response.end();
}
