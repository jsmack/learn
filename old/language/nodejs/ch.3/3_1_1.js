const http = require('http');
const fs   = require('fs');
const ejs  = require('ejs');
const url = require('url');

const index_page_file = './3_1_1.index.ejs';
const other_file = './3_1_1.other.ejs';
const css_file = './3_1_1.css';


const index_page = fs.readFileSync(index_page_file, 'utf8');
const other = fs.readFileSync(other_file, 'utf8');
const css = fs.readFileSync(css_file, 'utf8');

var server = http.createServer(getFronClient);

server.listen(8080);
console.log("start");

function getFronClient(request, response) {
    var url_parts = url.parse(request.url, true);
    switch(url_parts.pathname) {
        case '/':
            var content = "This is page";
            var query   = url_parts.query;
            if ( query.msg != undefined ) {
                var query_obj = content += ' you are [' + query.msg + '] get !';
            }
            var content = ejs.render(index_page, {
                title: "Title !!!",
                content: content,
            });
            response.writeHead(200, {'Content-Type': 'text/html'});
            response.write(content);
            response.end();
            break;
        case css_file:
            response.writeHead(200, {'Content-Type': 'text/html'});
            response.write(css);
            response.end();
            break;
        default:
            response.writeHead(200, {'Content-Type': 'text/plain'});
            response.write("failed....");
            response.end();
            break;
    }
}