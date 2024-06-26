# TL;DR
- 業務フローも良く確認する
- プログラム開発以外で解決する方法も検討する
- その方が先を見据えた効率化が進む場合もある

# 課題
<img src="https://1.bp.blogspot.com/-ZOg0qAG4ewU/Xub_uw6q0DI/AAAAAAABZio/MshyuVBpHUgaOKJtL47LmVkCf5Vge6MQQCNcBGAsYHQ/s400/pose_pien_uruuru_woman.png" width=150> 

「すみません、毎日行う業務の入力画面を直して欲しいのですが…」
「はい、どの様な改修依頼でしょうか？」
「毎日来る100枚前後の領収書／請求書を入力する画面の修正を…」

というような業務効率化の依頼があったとします。依頼者＝作業者ですね。
今時100枚前後の紙が特定の部署に届くという様な事は無いよ、と思った方は、
恐らくとても良い企業にお勤めです。
**こういう事は日常的に行われていたりします**。

:::note warn
紙の時代はまだ続いている。
:::

依頼者の希望通り、画面の構成等を変えることにより、
依頼者は紙から得た情報をコンソール上に入力する作業が軽減される事となり、
一定の作業軽減と、時短による効果を得る事が出来ました。
めでたし、めでたし。

…しかし、この問題は本当に解決したのでしょうか？

# 実態
依頼者に具体的に聞き取りを行い、この話を深堀りしていくと、
紙の書類を発生させているのは同じ企業の他部署の人員だという事が分かりました。
実態としては、以下の様な図となります。

![qiita_20240113_01.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/b760c2db-a5b4-3a1f-67f3-c221bb0fdee1.jpeg)

しかも、他部署の人員はわざわざ手書きで作成した領収書を、
入力させる為に依頼者に持ち込んでいた、という様な背景でした。

この方法では手書きで作成する時間は別途発生するし、
入力（転記）作業にも一定の時間と、転記ミスのリスクにも苛まれます。
依頼者が記載のチェックを行うことにより、
ちゃらんぽらんな領収書を突き返したりするというデータの正確さは担保されますが、
効率化と言う観点で言えば限界があるのはご想像の通りです。
この様な場合は以下の様に、業務フロー自体を見直すべきでしょう。
![qiita_20240113_03.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/e4146203-f305-1bc8-b9ad-046c6addf220.jpeg)
ログイン環境など、予定と違った改修が必要な場合もありますが、
環境によっては依頼者の入力画面をそのまま対象者に配るだけで、
業務効率化が進む場合もありそうです。
この方法は検討に値すると思います。

# 反発
とはいえ、この様な業務フローの改善において、大抵の場合は中々上手く行きません。
では障害となるのは何でしょうか？主な答えは、以下の部分です。

![qiita_20240113_02.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/35294b43-d6e7-d3f2-afc2-118952e706a8.jpeg)

これまで適当に依頼者に対して領収書を渡していた人物にとって、
この改善は**改悪に他ならない**のです。何故なら、

- 「適当にやっといて」が使えなくなる
- 期日を守らなければならなくなる
- パソコンの操作が苦手なのに、負担が増える
- やりたくねーよ！〇〇にやらせておけばいいだろ！

の様な、自分にとって不利益な内容が急に降り掛かるからです。
企業全体では得をしているのに、個人で見ると不利益を被るのを許容出来なく、
何故か反対勢力に回る人が多数になり改善が進まない、
というケースが高確率で存在します。

::: note warn
悲しいけどこれ、現実なのよね。
:::

しかし、ただでさえ忙しいと言うのに、
細々した仕事が増えるのが嫌だという気持ちも分からない訳ではありませんよね。

# 説得しないという選択は避けたい
こういう件において、**説得しないで、説明だけする**という手法があります。
決定という段階まで進めてしまい、
強引に実行段階に入ってしまうというパターンです。
これは遂行力という意味では非常に決定的なのですが、
社内での信頼を損なうという別の問題を抱える可能性があります。

説明責任は果たしたが、人間はそれぞれ感情があるので、
そこを疎かにしていると、いつかしっぺ返しを受ける可能性があります。
適切な手法で解決し、円満な形で改善を進めたいものです。

# 説明と説得
ここからがエンジニアの腕の見せ所です。
**得意の理論**と、**苦手な感情論**と、**交渉術**で敵を撃破しましょう。

## 理論ベースでの説得
業務効率化を行うという事は「**企業全体で見ると得をする**」という事に他なりません。
部署や個人レベルでは一定の負担を強いることになるかもしれないが、
結局は時間としての利益として計上される、どれくらいの効率化が見込める、
という事を**数値ベース**で伝えましょう。

企業は大抵の場合は営利団体ですので、
特定の作業が利益になるのであれば実施するのはやむなし、と考えられます。
これで「しょうがないか」と思ってくれれば儲け物です。

:::note 
DX化という言葉を積極的に使おう。昭和世代には効く。
:::

## 感情ベースでの説得
しかし、これだけでは内心納得出来ない方が存在します。
積極的に心的サポートを行いましょう。
具体的には操作のサポートや、作業増となる部署・担当者への心遣いです。
資料の作成も、相手の立場に立って作成しましょう。

操作が不慣れな人物が多いのであれば、
移行の為の並行期間／猶予期間等も積極的に長い期間採用し、
なるべく対象者に負担を掛けさせない様な方法で、
「時代の流れだし、しかたないか」と思ってもらう様に心掛けましょう。

:::note 
「〇〇さんもこの方法でやり始めましたよ」も結構効く。
:::

## 交渉術での説得
感情ベースでの説得に近い部分ではありますが、
負担の増加する可能性のある部署に対しては、**トップの首を獲りましょう**。
責任者に近い立場の方をとにかく説得し、反発を抑制する動きが必要です。
場合によっては自分の上長なども利用して、
「あの人が言うなら仕方がない」という感情も是非利用しましょう。

:::note warn
トップの説得を失敗するとヤバいので、実は分水嶺だったりもする。
:::

# 円満に、そして最善を
本件ではプログラムでの改善をほぼ行わず、
業務フローの整理だけで業務効率化の改善を行う手法でした。

これはエンジニアでなくても出来るじゃないか？という話でもありますが、
多くの場合、依頼者は権限を持たない作業者だったりします。
そして、彼らは**自分の作業の負担が軽減されれば良い**という場合がほとんどで、
その思惑に、前段の業務がどう行われているかまで、
想定や理解していなかったりすることもあります。

この改善は所謂「**プログラム的思考**」が用いられます。
どの様にデータが発生しているか、どう変えると最善になるのか、
我々エンジニアが得意とする部分なのです。

交渉だったり、説得だったり、人と関わる手法は苦手かもしれません。
なのでこの様な改善方法は面倒くさくて、採用し難いかもしれません。
ですが社内の業務効率化には、こんな改善方法が最善だったりもします。
業務効率化の依頼があった時には、是非その作業が必要な背景まで探ってください。
