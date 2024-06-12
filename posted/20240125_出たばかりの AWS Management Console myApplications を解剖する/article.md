# はじめに
AWS re:Invent 2023から、MCのホーム画面に突如登場したmyApplications。

https://docs.aws.amazon.com/ja_jp/awsconsolehelpdocs/latest/gsg/aws-myApplications.html

そんな昨年末からの新機能であるmyApplicationsですが、
それがどれかと言えば、MCのホーム画面に表示されている以下のwidgetになります。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/593ac97c-f1bf-29a0-bdd6-7bf6c122057d.png" width=500>

最近AWSのMCを開いていれば「ああ、それね」という方も多いと思いますし、
「そもそもMCなんて見ないな」と思う方もいらっしゃると思います。

:::note
MCを開いてない人もいるだろうし、
そもそもMCのホーム画面ってスルーしがち。
:::

## MCのホーム画面って見ますか？
ホーム画面はまじまじと見る派な私。
これに関して先日、面白い記事がありましたね。

https://qiita.com/inoue_d/items/e68f2c26578f33386f87

ホーム画面もカスタマイズ出来て便利だよ、という点には非常に共感なのですが、
記事の途中にmyApplicationsの画像出てますよね？
出てるけど、投稿者の最強widgetには入っていないので、途中で削除された…！？

::: note warn
myApplications、あまり使われていない予感しかしない。
:::

そんな残念感の強いmyApplidcationsですが、
myApplicationsはアプリケーション別のダッシュボードを簡単に作成してくれるもので、
これも詳しく説明してくれている記事があります。
とても分かり易い記事なので、興味のある方は以下をチェックしてみて下さい。

https://qiita.com/YSasago/items/f57b638943f51a454d7d

# myApplicationsとは何物なのか
ではmyApplicationsの話に入って行きます。
まず実際に「testApplication」という名称で、myApplicationsを作成してみます。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/eb8b7309-c0a2-b01e-e002-c55377f7056b.png" width=600>

リソースを特に指定せずそのまま作成して、ダッシュボードが完成しました。
なかなか便利ですね。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/f7068cb8-1c78-054b-657b-8ab955c55bed.png" width=600>

そして、気になるのはこの点。
※ID等が見えない様に一部黒塗りしています

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/750bd846-cfc2-ef79-57ec-91222246e918.png" width=300>

あれ、myApplicationsってResourceGroupsリソースなの？という点です。
しかも説明のところはアプリケーションタグ値、となっているし、ARNでも無さそう。

これが新規カテゴリのリソースであれば、
この部分がmyApplicationsとかになっていそうだな…と思いませんか？
そう、**myApplicationsという新規カテゴリは存在しないのです**。

それなら、myApplicationsは何者なのか、突き止めたい。
そういう部分を深堀りしてみたい、という事が本記事の趣旨になります。

# 調査
## Resource Explorerで探してみる
現在、自分のAWSアカウントには何もリソースを作成していない状態で、
ターゲットリソースも指定せずに、myApplicationsを作成した直後です。
Resource Explorerでどんなリソースが作成されているのか確認してみます。

リソースの検索画面で「testApplication」で検索すると、
3つのリソースが検索にヒットしました。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/aaa2e627-b3f1-14bd-04fd-56a3885a905f.png" width=600>

2種類がResourceGroupsに属したリソースであり、
もう1つがServiceCatalogに属しているタイプのリソースになっています。
どうやらMC画面上でmyApplicationsの作成操作を行うと、
これらの3種類のリソースをまとめて作成する様な動きになっている様です。
これらのリソースを見ていきます。

## ServiceCatalog
myApplicationsから作成されたServiceCatalogのリソースは、
AppRegistryのApplicationに属する物だという事が分かりました。
実際にmyApplicationsを削除する画面は、この画面に遷移するので、
「実態はServiceCatalogなんだな」と思った方もいたのではないかなと思います。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/9c0518ea-72ef-37d4-726c-8c21ce678574.png" width=600>

中身を見ると、恐らく同時に作成されたResourceGroupsのリソースが
関連付けされて結びついているのが確認出来ます。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/31513ff6-e456-131d-51ec-26532834da73.png" width=600>

## Resource Groups & Tag Editor
Resource Groupsの画面を開くと、これら2つが今回作成されたリソースでした。
何故2つあるのか？中身を見ていきたいと思います。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/ac22bb0d-b65c-a0da-8ec5-cadf4e5852f2.png" width=600>

まずは下の方のリソースから見ていきます。
こちらが先のServiceCatalogに結びついていた方のリソースです。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/aafc9655-b74f-2816-f785-88e4744c7142.png" width=600>

このグループに該当するリソースは、もう一つのResourceGroupsリソースだけでした。
もう一つのResourceGroupsリソースの中身も見て行きます。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/eb84c453-5ae8-930b-79bc-a3f2eb01af2b.png" width=600>

今回作成したtestApplicationではリソース指定を行いませんでしたが、
リソース指定を行った場合、このResourceGroupsリソースのグループリソースの部分に
指定したリソースが格納されています。
つまり、このResourceGroupsがリソース指定の**Object**ですね。

そして先に説明したResourceGroupsは抽象部分で、
**Interface**だったという事が分かりました。

## myApplicationsで作成される物
myApplicationsで同時に作成される物をまとめると、以下の3種類で構成されています。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/5e31410e-e475-98d2-eb92-1e91342a3382.jpeg" width=400>

最初に紹介したServiceCatalogはInterfaceであるResourceGroupsを参照し、
InterfaceはObjectであるもう1つのResourceGroupsを継承しています。
いわゆる、依存性逆転の法則が採用されています。

この3つを同時に作成し、これらの集合体を**myApplications**として、
様々な情報を参照できるダッシュボードを作成している事が分かりました。

# ってあれ？ServiceCatalogのApplicationって…？
ふと思った事ですが、
「**ServiceCatalogのApplicationって同時にResouceGroupも作らなかったっけ？**」
と気付き、myApplicationsを介さずに直接Application画面から作成してみました。
先程作ったmyApplicationsは削除して、また空の状態からスタートしています。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/10c2c57b-a297-2c7a-133f-aca082b6412b.png" width=600>

上記のように作成した後、改めてResourceGroupsの一覧を見に行きます。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/3d686ec3-3deb-4a8b-a239-55b7d9ff99f5.png" width=600>

**ResourceGroupsリソースも同時に作られていました。**

何ならmyApplications widgetにも出てきました。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/ec06dc96-05bd-e424-d55d-3f9ec8a7abd8.png" width=600>


つまり、myApplicationsが上記3リソースを作成している、というのは確かですが、
具体的にmyApplicationsが内部的にやっている事は、以下という事です。

- ServiceCatalogのApplicationリソースを作成する
- Applicationリソースを作成した時に同時に作成されるResourceGroupsのObjectに
初期設定画面上で指定したリソースを格納する


# おわりに
元はterraformで環境を構築する際に、
myApplicationsも一緒に作る様にしようかなと思ったのですが、
それらしきリソースカテゴリが見当たらなかった為に、
「これ何なんだろう？」と思ったのがきっかけでした。

MC上で操作すると複数のリソースを同時に作成していたりするので、
裏で行われている実態を解き明かすのも面白いものです。
また少しAWSについて詳しくなったような気がします。
