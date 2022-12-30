■ CHAPTER 5 L4プロトコル
● 5-01 UDP
- udp_header.pcapng
	UDPヘッダーを確認できるキャプチャファイル
- udp_firewall_accept.pcapng
	ファイアウォールがUDPデータグラムを許可しているときのキャプチャファイル
	PCが送信したUDPデータグラム（No.1、No.3）を、ファイアウォールが許可し、サーバーからレスポンスが返ってきている（No.2、No.4）
- udp_firewall_drop.pcapng
	ファイアウォールがUDPデータグラムをドロップしているときのキャプチャファイル
	PCが送信したUDPデータグラムをファイアウォールがドロップしているため、サーバーからレスポンスがない
- udp_firewall_reject.pcapng
	ファイアウォールがUDPデータグラムを拒否しているときのキャプチャファイル
	PCが送信したUDPデータグラム（奇数No.）を、ファイアウォールが拒否し、ファイアウォールからICMPパケット（Port Unreachable）が返ってきている（偶数No.）


● 5-02 TCP
- tcp_header.pcapng
	TCPヘッダーを確認できるキャプチャファイル
- tcp_header_iphone_curl.pcapng
- tcp_header_iphone_safari.pcapng
- tcp_header_macosx_safari.pcapng
- tcp_header_ubuntu_curl.pcapng
- tcp_header_windows10_chrome.pcapng
- tcp_header_windows10_curl.pcapng
- tcp_header_windows10_edge.pcapng
- tcp_header_windows10_firefox.pcapng
	OSやWebブラウザによって異なるTCPヘッダーを確認できるキャプチャファイル
- tcp_3whs_4wc.pcapng
	3ウェイハンドシェイク（No.1～No.3）から、4ウェイハンドシェイク（No.15～No.18）までの流れを確認できるキャプチャファイル	
- tcp_stream_option.pcapng
	TCPストリームオプションによって、エラーが発生しているコネクションを抽出できるキャプチャファイル
- tcp_duplicate_ack.pcapng
	重複ACKとFast Retransmitの動作を確認できるキャプチャファイル
	No.11と同じACKパケットがNo.13、No.15、No.17でも返ってきており、Fast Retransmitが発動している
- tcp_close_interruption.pcapng
	TCPコネクションを途中でキャンセルしたときのキャプチャファイル
	HTTPでファイルをダウンロードしている途中でキャンセルしたため、最後にRST/ACKパケットが返っている（No.733）
- tcp_close_unavalable_service.pcapng
	ダウンしているサービスに対してアクセスしたときのキャプチャファイル
	SYNパケットで3ウェイハンドシェイクを試みるものの（奇数No.）、RST/ACKパケットで拒否されている（偶数No.）
- tcp_firewall_accept.pcapng
	ファイアウォールがTCPセグメントを許可しているときのキャプチャファイル
	PCが送信したTCPセグメントを、ファイアウォールが許可し、サーバーからレスポンスが返ってきている
- tcp_firewall_reject.pcapng
	ファイアウォールがTCPセグメントを拒否しているときのキャプチャファイル
	PCが送信したTCPセグメント（No.1）を、ファイアウォールが拒否し、サーバー（実際はファイアウォール）からレスポンスが返ってきている（No.2）
- tcp_firewall_drop.pcapng
	ファイアウォールがTCPセグメントをドロップしているときのキャプチャファイル
	PCが送信したTCPセグメントをファイアウォールがドロップしているため、サーバーからもファイアウォールからもレスポンスがない
- tcp_syn_retransmission.pcapng
	サーバーから応答がなく、SYNを再送信しているときのキャプチャファイル
	表示フィルタに「tcp.flags.syn eq 1」を入力し、時刻表示形式を「前に表示されたパケットからの秒数」にすると、間隔を変えながら、SYNを再送信している
- tcp_delayed_ack.pcapng
	遅延ACKの動作を確認できるキャプチャファイル
	ACKパケットが少し（0.05秒）遅れて送信されていることが分かる（No.3、No.6、No.9、No.12）
- tcp_nagle_disable.pcapng
- tcp_nagle_enable.pcapng
	Nagleアルゴリズムを有効にしたとき、無効にしたときのキャプチャファイル
	Nagleアルゴリズムを有効にしていると、MSSにまとめて送信している
	Nagleアルゴリズムを無効にしていると、MSSになる前にどんどん送信している
- tcp_fast_open.pcapng
	Fast TCP Openの動作を確認できるキャプチャファイル
	最初の3ウェイハンドシェイク（No.1～No.3）でTCP Fast Open Cookieをやりとりし、2回目の3ウェイハンドシェイク（No.12～No.14）ではSYNからHTTPメッセージをやりとりしている
