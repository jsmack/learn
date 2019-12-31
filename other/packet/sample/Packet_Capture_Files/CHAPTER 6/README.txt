■ CHAPTER 6 アプリケーションプロトコル
● 6-01 HTTP
- http_request_get.pcapng
	サーバーのコンテンツをGETしたときのキャプチャファイル
	クライアントがHTTPで「8K」のコンテンツをGETし（No.4）、サーバーが応答している（No.6以降）
- http_response_200.pcapng
- http_response_302.pcapng
- http_response_404.pcapng
- http_response_503.pcapng
	サーバーがいろいろなHTTPレスポンスを返していることが分かるキャプチャファイル
- http_http10_notls.pcapng
	WebサーバーのコンテンツをHTTP/1.0でGETしたときのキャプチャファイル
	コンテンツごとにコネクションを作り、GETしていることが分かる
- http_http11_notls.pcapng
	WebサーバーのコンテンツをHTTP/1.1でGETしたときのキャプチャファイル
	最大コネクション数分のTCPコネクションを使いまわして、GETしていることが分かる
- http_http2_tls.pcapng
	サーバーのコンテンツをHTTP/2でGETしたときのキャプチャファイル
	1つのTCPコネクションを使いまわして、GETしていることが分かる


● 6-02 SSL
- ssl_handshake.pcapng
	SSL接続するためのSSLハンドシェイクをしているときのキャプチャファイル
	No.1～No.3でTCPの3ウェイハンドシェイク、No.4～No.9でSSLハンドシェイクが行われている
- ssl_web01.local.key
	ssl_handshake.pcapngを復号するときに使用するサーバーの秘密鍵
- ssl_resumption.pcapng
	SSLセッションを再利用しているキャプチャファイル
	No.23からSSLセッションを再利用しようとしている
	No.23のClient Helloには、No.5のServer Helloと同じセッションIDが含まれている
- ssl_client_auth.pcapng
	SSLでクライアント認証したときのキャプチャファイル
	No.8でCertificate Requestをして、クライアント証明書をリクエストしている


● 6-03 DNS
- dns_recursive.pcapng
	キャッシュサーバーが再帰クエリと反復クエリを処理しているキャプチャファイル
	「www.google.com」をrootから順に名前解決している
- dns_zone_transfer.pcap
	ゾーン転送をしているキャプチャファイル
	最初にSOAレコードを問い合わせ、その後ゾーンファイルを転送している


