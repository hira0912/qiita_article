# 発端
元ソース。

https://gigazine.net/news/20230913-nginx-unit/

nginx Unitを使うと、現在利用しているPHPのアプリケーションサーバPHP-FPMより
応答速度が８倍速くなるとかいう触れ込み。
赤い彗星もビックリ。

# ソフト概要
## PHP-FPM
https://www.php.net/manual/ja/install.fpm.php

PHPの標準アプリケーションサーバソフトウェア。
Webサーバーとして稼働する際に、
ブラウザからのリクエストによってPHPを実行する為のプログラム。
特に選択肢が無ければ使われる様な気がする。

## nginx Unit
https://www.nginx.co.jp/products/nginx-unit/

nginx.Incが出しているアプリケーションサーバソフトウェア。
PHPだけでなく、pythonやJavascriptなども実行する事が出来て、
マルチな言語に対応出来るのが魅力。
最近意外とはえーんじゃないかなと上記記事で少し話題になった。かもしれない。


# 実際に検証してみた
やってみないと良く分からないので、設定した上でベンチマークしてみる事にした。
サイトはAWS上で作成したテストサイト。実装済のサイトなので、画像読み込み等がある。
EC2はt2.microで作成。webサーバにはnginxを採用。

## ベンチマーク
計測の為のソフトはapache benchを使用。

https://httpd.apache.org/docs/2.4/programs/ab.html

サイトベンチマークソフトで、yum install httpd-toolsをした後に利用出来る。
裏ではリクエスト数や同時接続数を変えながらテストしたが、
今回は条件を500リクエスト、同時接続数50で実施した結果を以下に示す。
コマンドは以下の通り。アドレスの最後にスラッシュを入れないと動かない（１敗）

```
ab -n 500 -c 50 https://hogehoge.jp/
```

以下詳細結果。概要は別項目でまとめる。

<details><summary>PHP-FPM</summary>

```
Server Software:        nginx
Server Hostname:        hogehoge.jp
Server Port:            443
SSL/TLS Protocol:       TLSv1.3,TLS_AES_256_GCM_SHA384,2048,256
Server Temp Key:        X25519 253 bits
TLS Server Name:        hogehoge.jp

Document Path:          /
Document Length:        43877 bytes

Concurrency Level:      50
Time taken for tests:   75.685 seconds
Complete requests:      500
Failed requests:        69
   (Connect: 0, Receive: 0, Length: 69, Exceptions: 0)
Total transferred:      20336044 bytes
HTML transferred:       20248544 bytes
Requests per second:    6.61 [#/sec] (mean)
Time per request:       7568.488 [ms] (mean)
Time per request:       151.370 [ms] (mean, across all concurrent requests)
Transfer rate:          262.40 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        3   36  57.8      6     421
Processing:   383 7349 3370.4   7137   16983
Waiting:      281 2378 1321.5   2272    9458
Total:        388 7384 3385.5   7170   17135

Percentage of the requests served within a certain time (ms)
  50%   7170
  66%   8484
  75%   8949
  80%   9239
  90%  11292
  95%  15774
  98%  16567
  99%  16865
 100%  17135 (longest request)
```

</details>

<details><summary>nginx Unit</summary>

```
Server Software:        nginx
Server Hostname:        hogehoge.jp
Server Port:            443
SSL/TLS Protocol:       TLSv1.3,TLS_AES_256_GCM_SHA384,2048,256
Server Temp Key:        X25519 253 bits
TLS Server Name:        hogehoge.jp

Document Path:          /
Document Length:        43892 bytes

Concurrency Level:      50
Time taken for tests:   94.478 seconds
Complete requests:      500
Failed requests:        0
Total transferred:      22033500 bytes
HTML transferred:       21946000 bytes
Requests per second:    5.29 [#/sec] (mean)
Time per request:       9447.799 [ms] (mean)
Time per request:       188.956 [ms] (mean, across all concurrent requests)
Transfer rate:          227.75 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        3   13  25.1      4     138
Processing:   715 9015 1373.4   9156   11380
Waiting:      282 7916 1384.4   8080   10278
Total:        719 9029 1367.6   9164   11384

Percentage of the requests served within a certain time (ms)
  50%   9164
  66%   9416
  75%   9586
  80%   9697
  90%  10200
  95%  10503
  98%  10896
  99%  11154
 100%  11384 (longest request)
 ```
 
 </details>

 ## 検証結果総論
 以下に簡単にまとめた。
 
 |  | PHP-FPM | nginx-unit |
|:------:|:------:|:------:|
| 総時間 | 75秒 | 94秒 |
| リクエスト失敗数 | 69 | 0 |
| リクエスト時間平均 | 6.61秒 | 5.29秒 |

８倍速いかどうかは置いておいて、
PHP-FPMは応答していないケースが多発していた。
これは同時接続数が10くらいだと起きなくて、
同時接続数が増えるとリクエスト失敗数が加速度的に増えた。
nginx-unitはそれが無かったのは好印象である。
総時間はPHP-FPMの方が速いが、
リクエスト時間そのもので言えばnginx Unitの方が速かった。
何ならPHP-FPMはリクエスト失敗してるしな。

# 結論
今回初めて導入テストをしてみたが、結構悪く無いという印象。
nginx Unitの過去の評判だと、結局PHP-FPMの速いという記事も散見したが、
今の時点の印象では結構印象が覆っている印象を受ける。

