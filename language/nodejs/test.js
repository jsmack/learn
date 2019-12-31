var http = require('http');

// Webサーバーの作成
var server = http.createServer();

// イベントハンドラを登録する
server.on('request',function(req,res) {
    res.writeHead(200,{'Content-Type': 'text/plain'});
    res.write('Hello world\n');
    res.end();
})

// イベントの待機
server.listen(8080);