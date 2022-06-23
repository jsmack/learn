https://pages.awscloud.com/event_JAPAN_Ondemand_Hands-on-for-Beginners-Serverless-3_CP.html


https://www.youtube.com/watch?v=HXGoYmUQWZw&feature=emb_title

https://www.youtube.com/watch?v=BP8p_p9JTMM&ab_channel=AmazonWebServicesJapan%E5%85%AC%E5%BC%8F

- 連携パターン
  - lambdaがポーリングして関数を実行
    - stream
      - dynamodb変更時に呼び出す
    - stream以外
      - sqs
  - 非ポーリングでイベントソースから呼ばれる


- labmda
  - 関数
    - 同期的
      - api lambda
    - 非同期
      - s3 lambda
        - まずは受け付けて裏で処理をするとか
  - イベント
    - 読み取り(ポーリング：ストリームベース)
      - dynamodb
    - not 読み取り(ストリームじゃない)
      - sqs 


https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/lambda-services.html



https://www.youtube.com/watch?v=TXHSewoOhq8&feature=emb_title&ab_channel=AmazonWebServicesJapan%E5%85%AC%E5%BC%8F
- lambda
- s3

https://www.youtube.com/watch?v=Jbh5K4HH5-4&feature=emb_title&ab_channel=AmazonWebServicesJapan%E5%85%AC%E5%BC%8F
- transcribe
- s3

https://www.youtube.com/watch?v=EYx_mybt8zk&feature=emb_title&ab_channel=AmazonWebServicesJapan%E5%85%AC%E5%BC%8F
- lambda

https://www.youtube.com/watch?v=dgNvRBabG6o&feature=emb_title&ab_channel=AmazonWebServicesJapan%E5%85%AC%E5%BC%8F
- comprehend
  - 自然言語サービス
  - ポジティブネガティブ等を判断

https://www.youtube.com/watch?v=tsrQc3UKl_4&feature=emb_title&ab_channel=AmazonWebServicesJapan%E5%85%AC%E5%BC%8F
- polly
  - text から音声を生成