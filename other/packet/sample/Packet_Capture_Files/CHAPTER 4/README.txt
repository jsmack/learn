■ CHAPTER 4 L3プロトコル
● 4-01 IP
- ip_header.pcapng
	IPヘッダーを確認するためのキャプチャファイル
- ip_ipv6_header.pcapng
	IPv6ヘッダーを確認するためのキャプチャファイル
- ip_fragment.pcapng
	IPパケットがフラグメントされているときのキャプチャファイル
	Echo Requestが2つに分割されている
- ip_routing_pc1.pcapng
- ip_routing_r1.pcapng
- ip_routing_r2.pcapng
	PC1 --- R1 --- R2 --- PC2
	ルーティングの動作を確認するためのキャプチャファイル
	PC1（192.168.1.1）からPC2（192.168.2.1）に対して、Echo Requestを送信する
	PC1、R1、R2におけるヘッダー制御を確認できる
- ip_routingloop_pc1.pcapng
- ip_routingloop_r1.pcapng
	PC1 --- R1 --- R2 --- Internet
	R2のデフォルトルートが間違っていて、R1とR2でルーティングループが発生したときのキャプチャファイル
	最終的に、R1でEcho Requestが破棄され、PC1に「Time to live exeeded」が送信される


● 4-02 IPsec
- ipsec_decrypt.txt
	Cisco IOSとstrongSwan（@Ubuntu）をIPsecで接続したときの設定をまとめたテキストファイル
- ipsec_isakmp_esp.pcapng
	PC1 --- Cisco IOS ---（IPsec）--- strongSwan --- PC2
	Cisco IOS（10.1.1.1）とstrongSwan（10.1.1.2）をIPsecで接続したときのキャプチャファイル
	PC1（192.168.100.1）からPC2（192.168.200.1）に対してEcho Requestを送信し、Cisco IOS側からstrongSwanにIPsecを接続を試みる


● 4-03 ICMP
- icmp_request_reply.pcapng
	Echo RequestとEcho Replyをやりとりしているときのキャプチャファイル
	PC1が送信した「Echo Request」（奇数No.）に対して、PC2が「Echo Reply」（偶数No.）を返している
- icmp_net_unreachable.pcapng
	ルータが宛先IPアドレスに対するルーティングエントリを持っていないときのキャプチャファイル
	PCが送信した「Echo Request」（奇数No.）に対して、ルータが「Net unreachable」（偶数No.）を返している
- icmp_host_unreachable.pcapng
	ネクストホップが動作していないときのキャプチャファイル
	PCが送信した「Echo Request」（奇数No.）に対して、ルータが「Host unreachable」（偶数No.）を返している
- icmp_fragmentation_needed.pcapng
	ルータがフラグメントを要求しているときのキャプチャファイル
	PCが送信したDF=1の「Echo Request」（奇数No.）に対して、ルータが「Fragmentation Needed」（偶数No.）を返している
	ルータの出力インターフェースのMTUを1000バイトに設定しているので、「Fragmentation Needed」にMTU=1000が含まれている
- icmp_acl_filtered.pcapng
	ルータのACL（Access Control List）でICMPを拒否しているときのキャプチャファイル
	PCが送信した「Echo Request」（奇数No.）に対して、ルータが「Communication administratively prohibited by filtering」（偶数No.）を返している
- icmp_redirect.pcapng
	ルータが別のゲートウェイを伝えたときのキャプチャファイル
	PCが送信した「Echo Request」（No.1）に対して、ルータが「Redirect」（No.2）を使用して、別のゲートウェイのIPアドレス（192.168.124.4）を通知している
- icmp_tracert.pcapng
	PC1からPC2に対して「tracert」を実行しているときのキャプチャファイル
	PC1はTTLを1つずつ増やしてEcho Requestを実行している