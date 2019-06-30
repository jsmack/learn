■ CHAPTER 3 L2プロトコル
● 3-01 Ethernet
- ethernet_ethernet2.pcapng
	EthernetⅡのフレームフォーマットを確認できるキャプチャファイル
	HTTPやSMTPなど、一般的なデータ通信はEthernetⅡを使用している
- ethernet_802.3.pcapng
	IEEE802.3のフレームフォーマットを確認できるキャプチャファイル
	CDP（Cisco Discovery Protocol）やSTP（Spanning Tree Protocol）はIEEE802.3を使用している
- ethernet_broadcast.pcapng
	ブロードキャストとユニキャストのフレームを見ることができるキャプチャファイル
	Destination MACアドレスが「ff:ff:ff:ff:ff:ff」になっている（No.1）
- ethernet_802.1q.pcapng
	802.1qでVLAN2のVLANタグが付いたパケットをやりとりしているキャプチャファイル
	PC1（10.2.2.101） --- （802.1q）--- PC2（10.2.2.102） 
- ethernet_l2sw_pc1.pcapng
- ethernet_l2sw_pc2.pcapng
- ethernet_l2sw_pc3.pcapng
	L2スイッチに接続したPC1（192.168.1.1）、PC2（192.168.1.2）、PC3でそれぞれ取得したキャプチャファイル
	PC1からPC2に対してEthernetフレームを送信すると、PC3にもフラッディングされたパケットが飛んでいる
- ethernet_l2sw_mac-address table.txt
	L2スイッチ（Cisco Catalystスイッチ）のMACアドレステーブルの状態を表したテキストファイル
- ethernet_l2loop_pc1.pcapng
- ethernet_l2loop_pc2.pcapng
	L2ループが発生したときにPCで取得したキャプチャファイル
	ブロードキャストを使用しているARP Requestで埋め尽くされている


● 3-02 PPPoE
- ppp_pap.cap
	PPPでPAP認証したときのキャプチャファイル
	PAP認証はパスワードがクリアテキストで流れる（No.5～No.8）
	# ちなみに、認証成功後はOSPF（Open Shortest Path Fast）でルート情報をやりとりしている <--- OSPFは本書では取り扱っていない
- ppp_chap.cap
	PPPでCHAP認証したときのキャプチャファイル
	CHAP認証はチャレンジ値を使用して、パスワードを暗号化する（No.5～No.10）
	# ちなみに、認証成功後はOSPF（Open Shortest Path Fast）でルート情報をやりとりしている <--- OSPFは本書では取り扱っていない
- pppoe.pcapng
	PPPoEで接続したときのキャプチャファイル
	2つのステージを経て（No.1～No.23）、実際のデータ通信に移る（No.24以降）


● 3-03 ARP
- arp_request_reply.pcapng
	最も一般的なARP RequestとARP Replyの流れを表すキャプチャファイル
	「10.1.1.100」から「10.1.1.200」に対してICMPパケットを送信する前に、ARPのやりとりが行われる
	PC1（00:0c:29:ce:90:e4）がARP Requestで「10.1.1.200」のMACアドレスを解決しようとする（No.1）
	PC2（00:0c:29:5e:f5:ab）がARP Replyで応答する（No.2）
- arp_ip_duplicated.pcapng
	PC1（00:0c:29:ce:90:e4）にPC2（00:0c:29:5e:f5:ab）と同じIPアドレス「10.1.1.200」が設定されたときのキャプチャファイル
	PC1にIPアドレスが設定されると「10.1.1.200」のARP Requestがブロードキャストで送信される（No.1）
	それに対して、PC2がユニキャストのARP Replyで応答する（No.2）
