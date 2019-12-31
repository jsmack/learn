const http = require('http');

var server = http.createServer(
    function(request, response){
        response.setHeader('Content-Type', 'text/html');
        response.write('<!Document html><html lang="ja">');
        response.write('<head><meta charset="utf-8">');
        response.write('<title>Test</title>');
        response.write('</head>');
        response.write('<html><body><h1>hello</h1><p>ようこそ</p></body></html>');
        response.end('');
    }
);

server.listen(8080);
console.log('start');