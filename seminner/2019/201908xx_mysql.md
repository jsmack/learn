- GIS エンハンス
  - https://www.slideshare.net/yoyamasaki/mysql-80gisfoss4g-2018-hokkaido

- ロール設定
  - https://www.s-style.co.jp/blog/2018/07/2123/

- リソースグループで接続スレッドの処理優先度を変更

- 前のバージョンまではクエリーキャッシュという機能があったんですがMySQL 8.0から廃止
  - リソースグループの機能を使うことで優先度を下げれば、他サービスへの影響を軽減できる


- デフォルトのユーザー認証プラグインが変更
  - これまではmysql_native_passwordがデフォルトだったんですが、MySQL 8.0からはcaching_sha2_passwordがデフォルトになりました。






matsunobuさん

MySQL replication and HA @facebook

複数リージョンで構成している
１リージョンにつき１インスタンス

マルチマスタの運用は難しいので、シンプルな構成をチョイスしている
１マスタ -> 複数スレーブの２層構成

LBU -> facebookの特殊なサーバでbinlogのみ保存

wormhole binlogの更新情報をもとにmysql以外のDBを更新


binlogserver
https://opensource.google.com/projects/mysql-ripple



purge log

write  set replication



sysbench


ABS async behind semi-sync


binlogchecksum

