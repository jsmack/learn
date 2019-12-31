const http = require('http');
var server = http.createServer(
    // function(request, response) {
    //     response.end('http');
    // }
    (request,response)=>{
        response.end('http');
    }
);



server.listen(8080);
