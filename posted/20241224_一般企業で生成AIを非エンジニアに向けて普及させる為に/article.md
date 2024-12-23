# TL;DR
- 生成AIの普及には「**社内教育**」と「**仲間作り**」から始めよう
- 非エンジニアには「**習う機会の提供**」と「**難しさの排除**」を
- ガイドラインの制定も並行して行いたい

# はじめに
IT企業では無い、いわゆる一般企業においては、エンジニアは居ても従業員全体の数パーセント程度だったり、場合によっては数百人規模の企業でもエンジニアは1,2人というケースもあると思います。

そういった環境においては、エンジニアは「情報システム部門」なんて呼ばれる事もあり、筆者も「情シス」と呼ぶ方がロールとしては近い、そんなエンジニアの一人です。

## 生成AIへの興味関心
今、この記事を読んで下さっている方の多くはエンジニアだったり、少なくともITに一定の興味関心がある方だと思って記載していますが、世間ではエンジニアより、非エンジニアと呼ばれる人の割合の方が圧倒的に多いです。

表題の生成AIの話に戻りますが、2022年11月にChatGPTがリリースされ、2023年には流行語にも輝く程、あらゆる年齢層にまで認知された「単語」であると言っても過言では無いと思いますが、いわゆる非エンジニア層が積極的に使えているかと言われれば、そうでもありません。

適切に取り扱って利用する事が出来るか、といったレベルでは無く「一度触ってみた事がある人」でさえ数割、と言った様な程度でもあります。

**ITに興味があっても生成AIを使わない人もいる** し、<font color=red>**そもそもITに興味が無い人も多い**</font> のです。これから生成AIがどれだけ発展しようが、使わない人は当たり前のように使わない。生成AIの利用に関しては、いわゆる「個人の裁量」に委ねられます。

::: note warn
自分と他人の興味関心が、必ずしも同じとは限りません。
得意不得意だって人それぞれであり、そういう部分は許容すべきだと思います。
:::

## でも生成AIを社内で普及させたい！
企業において業務の効率化や、新たな発展を考えた時に、生成AIを積極的に活用してみようと考えた事のある人は多いかなと思います。しかしながら、自分が興味を持ったところで、自分の周りの人が同じように生成AIに興味があるかどうかは分かりません。

生成AIやITに興味・理解がある人が多い環境であれば「**生成AIの社内での普及**」という旅路はそこまで難しい物では無いと感じるかもしれません。では一般企業だと、どうでしょうか？

ITに興味関心がある人自体が圧倒的にマイノリティな世界で、生成AIを普及させる為にはどうしたら良いのか。実は筆者の取り組みもまだ、道半ばであります。完全に達成もしていないのに、胸を張って言える段階では無いかもしれませんが、既に実施した事、今後の展望など、織り交ぜて記載して行きたいと思います。



# 前提として
ビジネスにおける生成AIの使い方として、大きく二つに分けようと思います。
- 生成AIを個人レベルで利用する
- 生成AIをビジネスに組み込んで利用する

前者は生成AIを人間のアシスタントとして利活用し、個人の様々な業務の一部をサポートしてもらうと言った手法です。
後者はRAGなどの手法を活用し、ビジネスにおける製品／機能として活躍させる方法です。
どちらも生成AIの利用方法として有効であると考えますが、これらは別物として定義しておきます。

# 成長モデルと方針
生成AIを社内で普及させる為の成長モデル／ロードマップを以下のようなイメージで図示しました。

![スクリーンショット 2024-12-18 125911.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/fc3d846f-7bac-86f2-1d61-7cfed3cc6e58.png)

自分の周辺がどんなステージに居るかは人それぞれだと思いますが、私が勤めている企業ではステージ１とも言える「<font color=red>**生成AIを個人レベルで利活用出来る**</font>」レベルにまでも達していないと結論付けました。

先に述べた通り、筆者の勤めている企業は一般企業であり、非エンジニアが大半を占めます。多少偏見は混ざりますが、いわゆる20~30代の若者が多い訳では無く、ITに明るいと思われる人間はそれほど多くはありません。生成AIを触った事の無い人も多いかと思います。それ自体が悪い事だとは思いませんが、ただ**この段階からいきなり利益に結び付く様なアイデアや機能を作成するのは無謀である**と自分は考えます。

今読んで下さっている方々も、お勤めの企業は公的機関でも無い限り、営利団体がほとんどだと思います。その場合、生成AIを使ったビジネスが出来るか？の様な、何かしらの利益に結び付く事に着手したくなる事は理解出来ます。しかし、多少遠回りであっても「教育」や「仲間作り」を進めるのが近道だと、私は考えています。

::: note
まずは「**生成AIを知っている人**」を増やす事から始める事が近道だと思います。
:::

本記事ではこのロードマップの最序盤である、従業員が「生成AIを個人レベルで利活用出来る」様にする為に、どう取り組んでいるかを記載していきます。

## 何故一足飛びに製品作りに取り掛からないか
私の所属している企業には、確かに「情報システム部門」は存在しています。ですので、生成AIの開発について情シス部門が主導となり、他部門から見れば「**勝手に**」開発して何らかのサービスを作成・提供する事は出来ると思います。

しかしそれは勿体ない、と考えます。何故なら、生成AIを使って行いたいビジネスと言うのは「<font color=red>**アイデアが大事**</font>」だと信じて疑わないからです。

生成AIの生み出す内容は無限です。ひとつの突拍子も無いアイデアが、とてつもない利益を生み出したりする事もあると思います。そんなアイデアはエンジニアがいる部門だけが生み出すものではなく、**もっと他部門の人達が自ら発案したり、相談の中から生まれる物が最良**だと思っています。

生成AIで何かしらのビジネスを始めて利益を生もうと考えた場合、エンジニア側の少ないメンバー内でそれらに向き合って悩むくらいなら、新しいアイデアを生む事が出来るかもしれない様々な部門の「仲間作り」を社内で行う事が、より建設的であると考えます。それがこの様なロードマップを組んだ一つの理由です。

:::note 
狭い視点より、多角的な視点で見られる複数人の方が、
面白くて画期的なアイデアが生まれ易いと考えています。
:::

## 無理解との対立を埋める為にも重要
生成AIを適切に取り扱うには、理解が必要な部分がいくつかあります。その中で大きく影響を及ぼすのは「**ハルシネーション**」に関する問題でしょう。

これは生成AIがもっともらしく嘘を付いてしまう現象の事です。今の所、生成AIの回答についてハルシネーションを完全に回避出来る方法と言うものはありません。ビジネス上正確さを必要とする局面において、生成AIに全てを委ねる様な状況を採択する事は、まだ難しいと筆者は考えます。

しかし生成AIやITに無理解であれば「生成AIが絶対に嘘を言わない様にすれば良い」とか「生成AIが嘘を言うのはエンジニア側の手抜き」等と言われる状況が起きる可能性があります。あたかも生成AIが万能ツールであると言う様な誤認識と言うのは、未だに当たり前の様に存在し続けています。

この問題については**ハルシネーションを100％起こさない事は出来ないと納得してもらう**だけなのですが「エンジニアが出来ないと言う事は、手抜きであり嘘だ」という理論を発生させられると手が負えなくなるケースも想定する必要があります。後は「無理解者が勝手に不可能なプロジェクトを立ち上げる」とかもあり得ますね。

その時に「理解者」が多いと言うのは必ず役に立ちます。社内で一般的な生成AIの取り扱い方を定着させておく事も「理解者を得る事」の側面として重要であると考えます。

::: note warn
変なレッテルを貼られる前に、根回し的に適切な行動をしておくと、
後で動き辛くなる事は少なくなる、と考えます。
:::

# ターゲットについて
次に、教育のターゲットについて記載して行きます。筆者は、社内での従業員への教育方針について、ターゲットとして2つに分類しました。

- 生成AIを個人レベルで活用する人物
- 生成AIをビジネスで利活用する為の人物

イメージで言えば、前者はエンドユーザーであり、後者は運用やアイデア出しにも携わる人です。生成AIに興味のある方／今後関連の深そうな方は後者になり、それ程生成AIにあまり興味が無い人は前者になります。

ここでターゲットとなる人物像を切り分けた思惑として、
**興味の無い事への勉強が嫌いな人が存在する**事を考慮しました。

不必要な学習は要らない人、ただ自分に役に立つ事だけを知りたい、使えれば良いという人に対して、生成AIの理論などの話をグイグイ押すのは良くありません。例えば人によっては難しい、生成AIの仕組みに関する内容を説明しようものなら、拒否反応により却って理解の妨げになってしまう人も存在します。以上を考慮し、前者は必要な事だけをピンポイントで伝えるという狙いにしています。

::: note 
従業員全員が生成AIのプロになる必要はありません。
:::

## 生成AIを個人レベルで活用する人物とは
ターゲットについて。こちらは、生成AIを単純にツールとして使いたい人、というイメージで想定しています。一般的なデスクワークにおいても、生成AIが活躍する場面というのは大いにあると考えます。特に文章の草案作成や、英訳の初稿など、言語の分野において活躍する箇所は多いと思います。こういった方には主に、
- 生成AIの利用方法（プロンプトの案）
- ハルシネーションが起きるという事実の説明
- コンプライアンスの遵守

の様な部分を重点的に伝えて行きます。社内で疑問無く利用する分には十分な程度とし「最近出た新しい便利なツール」としての生成AIの使い方を学んでもらう事を目的としています。逆に苦手意識を持つ事で敬遠されない様に、とにかく「**優しい勉強**」を心掛けています。エンジニア側から注意深く歩み寄って、技術を習得してもらう、という意識が重要だと思います。

## 生成AIをビジネスで利活用する為の人物とは
こちらは先に説明した「仲間」としてイメージしています。ビジネスで利活用する際に、新たなアイデアを出してくれるかもしれない、そんな人達を想定しています。個人レベルで活用する人物に教育した内容の他に、
- ハルシネーションが何故起きるか（統計的推論の概念）
- 生成AIの回答結果に対する責任の考え方
- （特殊な）自社と生成AIの関連性の事情

等の内容も学習内容に加えます。このターゲットの方達には「こんな内容なら生成AI使えるかも」という判断が一定出来る、という事をゴールにしています。

::: note 
こちらは「プロ」として考えていますが、当然開発の知識まで要求はしません。
あくまで**ビジネスで利活用出来る**という人材のイメージです。
:::
以上の様な形で２種類のターゲットとして分け、教育内容や実施タイミングも分けて教育を行っていきます。実際は先に「仲間」を増やしておきたいので、先に教育するのは後者の方々です。

# 教育内容
ここからは、具体的な教育内容について記載していきます。
実際に社内で勉強会を既に行っている為、発表用の資料なども存在しますが、機密事項等もあるので本記事には内容のみ掻い摘んで記載します。

## プロンプトエンジニアリングについて
いわゆる生成AIの使い方の肝とも言えるプロンプトエンジニアリングですが、そもそも生成AIを触った事が無いという人がいる前提なので、この部分を筆者はhands-onで実施しました。実際に画面を見てもらい、そこで入力をした結果どんな結果が返ってくる、というのを見て学習してもらうという手法です。

- google検索等でも代替出来そうな語句についての質問
- 要約や英訳などの言語野に関する提案
- 各種シチュエーションにおける様々な提案の例

上記の様に、個人レベルでも比較的簡単に行える例にて実施しました。様々な使い方が出来るという事を実際に示して行く事で、有用性を分かってもらうという狙いがあります。

但し、このhands-onの中で、生成AIが特にハルシネーションを起こし易い「歴史上の人物」等の情報を聞いたりして、**事実と異なる情報を出してもらう**事はポイントです。後に繋がります。

## ハルシネーションについて（統計的推論について）
ハルシネーションの理解は生成AIを取り扱う上で重要な事項です。ただ、これについては「ハルシネーションは起きる前提で考える」という事を納得してもらう、という事で十分だと思っています。必ず「<font color=red>**人間がその結果を確認する**</font>」という事を説明するだけです。

プロンプトの調整等で、ハルシネーションが起きる確率を減らす努力をする事は出来ます。ただしどこまで行っても、精度は上げられるが、その精度は決して100％にはならないという事を理解してもらう事の方が重要です。

しかしながら、生成AIについて詳しく興味がある方なら、何故生成AIは嘘を言うのか？嘘を言わない様には出来ないのか？という疑問に行きつくはずです。また「生成AIが嘘を付く理由」について説明出来る必要が出る場合もあります。

この理由は「**統計**」に基づく知識と説明が必要なのですが、この疑問の根底には「プログラムなのに何故一意に正しい答えが決まらないんだ」という部分があるのかなと思いました。筆者は、この部分を「電卓と違い、答えがただ一つ決まる仕掛けではなく、**生成AIはみんながこう言うから、と言って回答を出すシステム**」という様な形で説明しました。
（この短文での説明は、正確な理解として適切な表現では無いのは理解しております。補足しておきます）

## 回答結果に対する責任の考え方について
ビジネスにおいて生成AIを取り入れたアイデア出しをしようと考えた時に、もう一つ重要な前提知識は「**責任**」の考え方だと思っています。

**生成AIは回答結果に対する責任を持ちません**。これはどの生成AIの製品でもそうです。

例えばwebのサービスがあったとして、生成AIが作成した文章をそのまま確認もせず企業の記事としてしまうのはあまりにも無責任である、という認識が重要です。人間の確認が必要、という事は、<font color=red>**生成AIが作成した文章については人間が責任を持って利用する**</font>、ということの徹底が必要だということです。

また、業務効率化等の目的で生成AIを使おうと考えた場合に、既に人間が担当している全ての業務を丸ごと生成AIに託すと言ったアイデアは、即採用が難しいと考えます。今、ビジネスにおいて人間が作業している作業については、**大抵の場合その作業者が作業の結果に対する責任を負っています**。それを生成AIに全て託してしまおうと考えた場合、<font color=red>**誰も責任を取らない**</font>という事が起きてしまい、ビジネスとしての責任モデルが成り立たなくなってしまいます。

こういった事を考えた場合、生成AIを採用する時に「生成AIをひとりにしない」ことを考えるのが肝要であると考えます。どの場合においても確認を人間が担当するというのが適切です。ケースによっては確認に関する工程を従来型のプログラムで担当するというのもアリだと思います。

::: note 
無責任に生成AIに全てを託して、楽が出来る訳ではありません。
:::


# 教育の手順について
ここまでは教育の内容と、ターゲットについて記載してきました。
後は、勉強会の開催を実施して行きます。

## 勉強会の開催
ようやく勉強会の開催です。出来れば自分の部署の周り、少なくとも自分の部署（上長がいるなら上長まで）の方は引き込めるようにしておいて下さい。周辺の部署でも興味のある方がいれば積極的に誘ってみるのが肝要です。

ここでのターゲットは、初回は比較的狭い範囲で良いと思います。但し、先に述べた様に上長がいるのであれば、その方からの理解が得られる様に強くプッシュして下さい。それは次以降、さらに範囲を拡大して勉強会を開き、さらに普及する為の布石になります。

::: note
筆者自体の社内での「権限」はさほど高い訳ではありません。
普及させる影響力を得る為には「権限」を持った人を巻き込む必要があります。
:::

必要なら勉強会を数回に分けて実施し、少しずつ地盤を固めると良いかと思います。但し勉強会に参加出来ないという事情がある人も当然居るので、時間をズラして開催したり、録画などの手法を使うのもアリだと思います。

# 生成AI利用ガイドラインの制定
勉強会が一定進むと、当然起きる問題があります。それは**ガイドラインの制定**です。
個人情報や機密事項を生成AIに入力しないとか、どの製品を利用したら良いのかなど、さらに生成AIの利用者が増える事を考えた時に、社内のルールとして、決めて行かなければならない事が無数に出てきます。
勉強会を拡大すると同時に、もし社内でガイドラインの制定が適切に行われていないのであれば、同時並行して作成する事をお勧めします。この決め事に関しては、単純に情報システム部門単体で決められる物でも無いと思うので、労務担当等との連携が必要かもしれません。
勉強会により生成AIの利用方法が学習出来たとしても、ガイドラインが未熟で、実際に社内で利用出来ないのであれば学習効果は無いものと同義です。より広い範囲に拡大する前に、事前のルール決めを先手を取って行いましょう。

::: note
無法地帯で不適切に利用される事を避ける為に、
適切なガイドラインの設定を早期に進めましょう。
:::

# ちなみに開発も併せて行っています
「一足飛びに開発を行わない」と言いつつ、実際には生成AIを利用したRAGの開発も一部で実施しています。これはまだ自社では研究段階ですが、実際に新しいプロジェクトが発生した時の検証も兼ねており、今回の普及が適切に広まった時、ひとつの案として提出出来る様にする為の物でもあります。

# おわりに
私の勤める企業では、まだ非エンジニアが生成AIを利活用出来るという段階に達していないと思います。しかしながら、それは「**分からない**」とか「**なんか怖い**」とか、意外と小さなきっかけで変わる物かもしれないと思っています。
生成AIは便利なツールです。使い方さえ適切に守れれば、デスクワークにおける様々な作業のサポートを行い、作業効率の向上に貢献する事が可能だと感じています。
非エンジニアにとって大事なのは「**習う機会の提供**」と「**難しさの排除**」です。この部分は、同じ企業に勤める物としてエンジニアが歩み寄れば提供出来る物です。今は生成AIについて否定的な人も、見方が変われば味方になるかもしれません。

:::note info
皆さんも、お勤めの企業で生成AI、広めてみませんか。
エンジニアと非エンジニアが適切にタッグを組むことが出来れば、
きっと面白い製品が作れると信じています。
:::