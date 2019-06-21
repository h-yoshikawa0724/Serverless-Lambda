### 参考
- Docker環境作成  
[Dockerで Serverless Framework 環境構築](https://qiita.com/seiichi_akiba/items/d42bda576f3fc6ac5117)

- QiitaいいねランキングAPI  
[Qiitaいいね数ランキングAPIの作成](https://qiita.com/zonbitamago/items/1027b532b174e5ee04b3)

- Slackへ特定の文字列でのリンクの作成  
[Slackのメッセージにて任意の文字列にリンクを埋め込むことはできますか？解決済](https://teratail.com/questions/80285)

### Docker環境

#### 注意点  
※Dockerfileにも記載はしているが、うまくいかなかった場合

serverless-python-requirementsをインストールする際、  
マウントしたディレクトリの中であるとエラーになるので、マウント外のフォルダに移動してからインストールコマンド実行  
`$ npm install --save serverless-python-requirements`

### コマンド

- Dockerコンテナに入る  
`$ docker-compose exec serverless sh`

- Serverless雛形作成(Python)  
`$ sls create -t aws-python`

- デプロイ  
`$ sls deploy`

- ローカルで動作テスト  
`$ sls invoke local -f ファンクション名`