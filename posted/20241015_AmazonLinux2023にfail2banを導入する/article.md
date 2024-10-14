# はじめに
AWSでEC2をベースに何かしらのWebサイトを立ち上げ、
DDoS攻撃を対応しようと考えた場合、
基本的にはAWS WAFを導入して対策しよう、と考えるのが適切かと思いますが、
その為にはApplication Load Balancerを導入する必要があり、
小規模でモノリシックな環境で十分、と考えるケースにおいては
コスト的には不釣り合いで、導入を見送るという事もあるかと思います。

そんな状況において、RHELベースのOSを利用していたのであれば、
<b>fail2ban</b>を選択肢に入れる事は大いに考え得る事ですが、
OSにAmazonLinux2023を選択した場合、従来通りの手法ではインストールが難しいので、
本記事ではそこに焦点を当てて行きます。

# 何故fail2banを導入する事が難しいか
## AmazonLinux2023のyumリポジトリ内に無い
al2023のデフォルト状態から、dnfによるfail2banのインストールは出来ません。
理由は単純で、al2023のyumリポジトリ内に存在していない為です。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/6163abb2-569f-dc85-6856-4eb7508c50bd.png)

## AmazonLinux2023にはEPELが導入出来ない
RHELベースのOSを利用していて、かつてfail2banを導入して来た人にとって、
考え得るインストール手順は<b>EPELリポジトリ</b>を導入する事だと思います。

筆者もその内の一人で、同じ様にAmazonLinux2023でEPELを導入しようと思いましたが、
AmazonLinux2023ではEPELをサポートしておらず、この手法を使う事は出来ません。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/1466b74b-4558-21a7-29c1-3fda8672aab9.png)


# インストール手順
fail2banをインストールをする為には、直接buildを行います。
インストールするパッケージは、githubから取得します。

### python3-develの導入
まず、python3-develをインストールします。インストール済なら本作業は不要です。

```
sudo dnf install python3-devel
```

### 作業用ディレクトリに展開
作業用ディレクトリ/tmpにwgetでパッケージを取得し、tarで展開します。
作業する場所はホームディレクトリでも構いません。

```
cd /tmp/
wget https://github.com/fail2ban/fail2ban/archive/refs/tags/1.1.0.tar.gz
tar -xzvf 1.1.0.tar.gz
```

### fail2banサービスの作成
fail2banのインストールと、サービスの作成を行います。

```
cd fail2ban-1.1.0/
sudo python3 setup.py build
sudo python3 setup.py install
sudo cp ./build/fail2ban.service /etc/systemd/system/fail2ban.service
```

このままサービスを起動したくなりますが、その場合エラーが発生して起動しません。
正常に起動する様に修正する為、fail2banサービスの設定ファイルの修正を行います。

<details><summary>起動に失敗した画像サンプル</summary>

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/14144046-4d77-5bb3-00d2-e734297e10f4.png)

</details>

### サービス設定ファイルの変更
コピーして作成した、/etc/systemd/system/fail2ban.service の修正を行います。
以下のEnvironmentの箇所です。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/fdf7e8ef-c334-d1bc-e009-dbe64373b519.png)

ここに先程インストールした、python3-develを指定します。
具体的には、以下の様に書き換えます。

```
Environment="/usr/local/lib/python3.9/site-packages"
```

### サービスの再起動／自動起動有効
最後に、サービスを再起動し、自動起動も有効にしておきます。
systemctl statusにて、正常に起動しているかどうかも確認します。

```
sudo systemctl restart fail2ban
sudo systemctl enable fail2ban
```

<details><summary>起動に成功した画像サンプル</summary>

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/f33ce225-ff33-7441-e165-b3295c96d266.png)

</details>

# コマンド一覧
お急ぎの方はこちらからどうぞ。
```
# python3-develの導入
sudo dnf install python3-devel

# 作業用ディレクトリにて展開
cd /tmp/
wget https://github.com/fail2ban/fail2ban/archive/refs/tags/1.1.0.tar.gz
tar -xzvf 1.1.0.tar.gz

# fail2ban serviceの作成
cd fail2ban-1.1.0/
sudo python3 setup.py build
sudo python3 setup.py install
sudo cp ./build/fail2ban.service /etc/systemd/system/fail2ban.service

# サービス設定ファイルの変更
sudo sed -i '/PYTHONNOUSERSITE/a Environment="PYTHONPATH=/usr/local/lib/python3.9/site-packages"' /etc/systemd/system/fail2ban.service

# サービスの起動
sudo systemctl restart fail2ban
sudo systemctl enable fail2ban
```