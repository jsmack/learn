const http = require('http');
const fs   = require('fs');
const ejs  = require('ejs');
const url = require('url');

const index_page = fs.readFileSync('./2_4_1.htm', 'UTF-8');
const style_css = fs.readFileSync('./2_4_1.css', 'UTF-8');
var server = http.createServer(getFromClient);


server.listen(8080);
console.log('start!');

function getFromClient(request, response){
    var url_parts = url.parse(request.url);
    switch(url_parts.pathname) {
        case '/':
            var content = ejs.render(index_page, {
                title: "This is index pages",
                content: "template page"
            });
            response.writeHead(200, {'Content-Type': 'text/html'});
            response.write(content);
            response.end();
            break;
        case '/2_4_1.css':
            response.writeHead(200, {'Content-Type': 'text/css'});
            response.write(style_css);
            response.end();
            break;
        default:
            response.writeHead(200, {'Content-Type': 'text/plan'});
            response.end('no!!!');
            break;
    }


}
