# はじめに
- 本記事では、自分が作成して実際に発表で使用したプレゼン用資料について、
勤務先の社内情報を抜いた上で、ほぼ全編に渡って掲載しています。

- 権利的にダメな物があった場合は画像を変更・または削除しますので、
その様な物があればコメント欄でご指摘下さい。よろしくお願いします。

# 背景として
私が所属している部署では毎週金曜日の午後に定例ミーティングがあり、
昨年から部内メンバーで持ち回りで勉強会を実施しています。

持ち時間は大体**30分前後**を目安として、
各々共有したい知識や、今開発している何かをプレゼン形式で説明しています。
意見交換や知識共有の他、プレゼン力や、資料作成の向上を目的としています。

:::note 
社内勉強会、いいよ。是非やりましょう。
:::

本記事の投稿日である2024/1/19(金)は、私の担当の日でした。

## 金曜日の午後は眠い
じゃあこの時間にやるな、という話ではありますが、
どう考えても**金曜日の午後は眠たい**という背景があります。
しかも昼飯を食った後ですから。これがいきもののサガか…

皆そういう事が分かって来た関係で、
**退屈しない**という事を考慮した資料作りや、構成で発表をする様になりました。
ある種のエンタメとして楽しみながら学習が出来る、
良い勉強会になりつつあります。とても良い事だと思います。

:::note info
聞いてもらえる為の努力や工夫、マジで大事。
聞いてもらえないと、話す意味が無い。
:::

## テーマにAWS Cognitoを採用したが…？
私は、今回の発表のテーマは**AWS Cognito**にしようと思っていました。

https://aws.amazon.com/jp/cognito/

AWS CognitoはAmazonが提供しているログイン認証システムで、
これを採用する事で様々なメリットを得る事が出来そうです。

この製品を自社で提供しているサービスでも採用出来るかもしれない。
発表のテーマとしては十分じゃないか！と思い事前調査をしていましたが、
AWS Cognitoと自社サービスの親和性があまり高くない事が分かって来て、
実際に**AWS Cognitoを採用するには至らないだろうな**、という結論に至りました。

:::note warn
必ずしも調べた事が生かせる訳では無いよね。仕方ない。
:::

## ひらめきに電撃落ちる
このままでは自社で使えないサービスの発表になるので、それは旨味が無いよな、
テーマ変更も視野に入れようかな、と考えていました。
しかし丁度[PHPカンファレンス北海道2024](https://phpcon.hokkaido.jp/)をオンライン視聴していた時に、電撃落ちる。

**社内で誰もLT(Lightning Talk)やった事ないし、
何ならLTという物自体知らない可能性さえあるし、
LTで発表をするという事自体を発表にしてしまえばいいんじゃね？**

という事に気付きました。目からウロコ。
これが今回、LTでAWS Cognitoを発表しようと考えたきっかけとなります。

# 発表内容
## 導入部分
この日もこれまでの発表の様に、30分程度の時間で発表する事にしてあったので、
部内の皆もそのつもりでいるという前提で、**謎の雑談枠**からスタートしました。

通常の30分程度で行う内容の講演であればムダでしか無い時間ですが、
本発表はLTでするので、時間的余裕があった為、全力で誤魔化しました。
その内容は部内向けの物なので割愛しますが、流れでLTの紹介に入って行きます。

話のきっかけを振って、
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/b160abaa-70d0-99bf-b65c-879f59e2f722.png" width="600">

問いかけを振って、
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/e3933106-5c99-cec1-d870-78e8df7dbe61.png" width="600">

カッコいい背景付きで紹介。
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/8c01f39d-d87c-49e6-3b08-7a58ba8e0d2f.png" width="600">

電光石火な紹介。
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/adac8f97-288c-7043-f616-3c1622036c16.png" width="600">

先日のPHPカンファレンス北海道2024でも実施されていますよ、
connpass等で行われる勉強会等でも使われていますよ、というアピール。
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/58540b7d-4794-6113-1305-909f29384cc4.png" width="600">

だから、今これからIT業界で羽ばたいて行く為にも、
１回くらいLTで発表してみようぜ！という強い呼びかけを行いました。

## 時間設定の悩み
当初、私は**５分**で発表を終えようと思っていました。
ですが、Amazon Cognito自体を知らないメンバーの為に、サービス内容の説明やメリット、
さらに機能的に自社サービスとの親和性が高くない事から、
本サービスの採用は難しいだろうと感じた事、という帰結まで伝える事が、
本発表を行う意義として、説明するべき内容だと思いました。

その為、全体としてのアジェンダは以下になりました。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/883e4818-9d5d-fc90-9ea0-bd05fb8cee91.png" width="600">

ここで起きた問題は、どうやっても時間が**５分では足りなかった事**です。

:::note warn
5分でやるには無謀だった。
:::

内容を削った上で全力で走って、最終的に**7分半前後**の発表時間にまとまりましたが、
これは5分でも10分でも無い微妙な時間であり、**スリリング感が足りない**と思いました。

せっかく皆にとってほぼ初めてのLT講演なのに、
**時間ギリギリを攻めないのは失礼**かと思いました。これは私の持論です。

なので、方針を大きく変えました。
時間設定を撤廃し、代わりに今回の発表のテーマを以下に定めました。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/902c7c8d-adf7-6ddd-8990-6b43046beae0.png" width="600">

予定時間を**７分**に定め、
そこを目標に全力でLTするというRTA(Real Time Attack)形式にしました。
意味分からないね。やってる自分も意味が分からなかったです。

https://dic.nicovideo.jp/a/rta


## タイトル＆自己紹介
部内メンバーに対して、事前情報として、
プレゼン用資料のタイトルのスクリーンショットは公開してありました。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/e6e736d2-ec4b-078e-e4d6-8707f4a9a885.png" width="600">

これはフェイク画像でした。実際に利用したのは以下です。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/341bb16e-5633-946c-522f-c10b2c8fbd8d.png" width="600">

部内でタイトル詐欺をしたのは、**RTAをするのがバレるから**です。すみませんでした。
上記は[RTA in Japan 2023 winter](https://rtain.jp/rtaij/rta-in-japan-winter-2023/) の壁紙を拝借しています。
いつも楽しく視聴させて頂いています。ありがとうございます。

タイトル詐欺をしていた事の弁明は、[エルシャダイ](https://elshaddai.jp/)がカバーしてくれました。
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/3f6cda64-c7cc-4e5b-2b00-47fe142025b8.png" width="600">

偽タイトルの時のイーノックはフルボッコにされましたが、
今の世界線は「**一番良い装備を頼んだ世界線**」なので、大丈夫だ、問題ない。

自己紹介は雑に行って、本編に入りました。
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/be7b0ceb-9d87-eeb6-1a66-0e7faa009679.png" width="600">
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/ea881bfa-e7d5-6027-0834-2edd9386047b.png" width="600">


## 本発表
ふざけ続けているとはいえ、本発表はマジメに行いました。

非エンジニアも参加している事を一定考慮して、
なるべく文字数を減らし、１枚のスライド当たりの情報量を減らして視認性を高めたり、
画像やアニメーションで直感的に今どの部分の話をしているのか、
スライドだけでは分からない情報は全てトーク部分で補う様にする、
等を意識して作成しました。

以下は概要部分です。
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/146eb55a-910d-1627-d146-94d74dea993b.png" width="600">
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/8f07f834-0703-cbff-f5d6-5ed50d81920f.png" width="600">

デフォルトでUIを利用出来るのは便利ですよね。社内サービス目的では利用しませんが。
自社UI画面が出ているので、見せられないよ！
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/1b566092-a07d-af09-2b1f-192717126fa4.png" width="600">

フェデレーションアクセスの話。
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/ea1cc0cc-6e9d-071c-c98d-36313398b97c.png" width="600">

MFAの話。自前で設置するのは大変なので、これも便利という話です。
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/2b0d6e3f-0fe6-9167-b4f7-d8116ef3035c.png" width="600">

続いて、メリットの部分に入っていきます。
可用性／耐障害性の話。
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/9925b8c0-8f89-f304-4625-6f152f0e7b77.png" width="600">

セキュリティ面の話。自前でセキュリティ維持するのは大変。
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/e1504c48-a9c1-0ca7-f076-2baa40325af4.png" width="600">

続いては自社サービスでの実装における問題点に入る所ですが、
その前に唐突に宣伝を入れてみたりしました。急いでいるんだよこっちは！
でも皆さん「広告をスキップ」押した事ありますよね？

Lightning Talkしている間は、**君も[無敵時間](https://t.co/hPMkZ1YMo1)になれるかもしれない。**
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/4a6f5c27-f49d-a28a-5ecc-30d41d362618.png" width="600">

自社サービスでの導入における問題点は、DB移行に問題があると考え、
そこを重点に説明しました。
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/a1155c64-e622-a061-10f4-76c2f4e68782.png" width="600">

顧客のターゲット層の問題で、ID自体は移行出来たとしても、
初回ログイン時に要求されるパスワード設定をユーザ側がクリア出来ず、
ユーザがサービスの利用を継続出来ない／クレームになる、
という事を考慮する必要があり、
社内システムで利用を開始する時の親和性が非常に悪いという結論に至った話です。
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/1cc1e57b-4e31-7855-89af-e7b9ef94a610.png" width="600">

::: note warn
この点に関しては、AWSに詳しい方であればlambdaトリガーを利用した方法で、
移行に近い形でパスワードの再登録の問題を解決出来る、
という内容自体は投稿者も承知しておりますが、
これとは別に他クラウドからの移転等の他の要素を抱えている為、
内容としては上記手段を取る事が困難と判断した、という事を追記しておきます。
:::

もう１点問題点を話しましたが、それは内部的な話なので、ここでは話せません。割愛。
と言ったところでまとめを話して、**タイマーストップ**となりました。
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/ef9a5383-945e-a065-61c8-e22073a9a2a3.png" width="600">

## 『世界一位』でした
記録を計ってもらっていましたが、**6分30秒**というタイムでした。
なんと、目標タイムの7分を切る事が出来ました。
ただ、少しばかり早口になり過ぎた感もあるのが反省点です。

実はこのタイトルとカテゴリで、かつこの資料でRTAを走った人は私しかいません。
つまり、名実共に**私が『世界一位』です**。異論は認めません。

## 完走した感想
完走した感想ですが、非常に疲れました。
<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/d5412981-0774-3346-5a5a-89abef5f373b.png" width="600">

この様に一般投稿する事を想定して作成した資料ですが、
皆様のLightning Talkでの発表の参考や、一助になればと思い投稿した次第です。
皆様も社内や社外での勉強会で、是非LTをやってみて下さい。
私も今年は色々な所でやってみたいなあと思い、この様な発表と、投稿をしました。

:::note info
ちゃんとまとめた資料は、別途社内で共有しました。
当たり前だよなぁ！
:::

長い記事となりましたが、ここまでお読み頂きありがとうございました。
今後の励みになりますので、良かったら:heartbeat:を押していって下さい。
X(twitter)の方もフォローしてね！:relaxed:
