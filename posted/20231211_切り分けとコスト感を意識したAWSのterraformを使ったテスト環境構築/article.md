# 経緯
## 構築サンプル
![Drawing 2023-12-11 10.40.15.excalidraw.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/952e1ec7-8359-e4f1-03f5-6829b46dc54f.png)

ざっくり、こんな感じでひとまとめの構築をterraformにて作成したとする。
これで作成されるのは、VPC、subnet、security group(以降SG)、EC2で、
作成順は自動的に判断された上で処理されて、VPC→[subnet,SG]→EC2となる。
削除時はこの逆順となり、EC2→[subnet,SG]→VPCの順。
これは関連リソースが残っていると削除できない様になっている為で、
VPCを消す時にsubnetが残っていたら、AWS側でVPCは削除できず、エラーになる。
AWS側で各リソースの依存性を守っているということ。

## こ、ここ、構築が消せない！
![Drawing 2023-12-11 10.40.16.excalidraw.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/a417dfbf-8f20-7c8e-c7eb-0a274c8ab923.png)

上記をふまえた上で、terraformの構築外部にlambdaを配置する。
terraformでlambdaも管理出来るが、ソース管理が相当複雑になる為、
基本的にはterraform構築外部に配置する事が望ましい。
ただこの場合、lambdaを消すか、各依存関係を切らない限り、
EC2以外のリソースを削除出来ない為、terraform構築の破棄が不可能になる。
テスト環境でEC2やRDS等、コストが発生するリソースを生かしておく必要が無い場合、
これは致命的で、構築をテスト時間外までずっと動かしておく必要がある為、コストが高い。

## terraformリソース分離によるコスト感の解消
![Drawing 2023-12-11 10.40.17.excalidraw.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/483bfccd-7c60-7a04-8e1b-4d98644bd4b6.png)

なので、こうしようという話。
コストが掛からない/微小な部分である、いわゆるインフラ部分でひとまとめ、
EC2,RDS等コストが掛かる部分について、いわゆるサーバ部分でひとまとめにする。
これならEC2消せるやんけ！という事で、
終業後はコストリソースだけ消して帰れば、コスト節約出来るよねという話。
ずっと残しておきたい部分と、入れ替えしたい部分を切り分けると
便利にテスト環境が作れるんじゃね？という様な内容。

# 構築手順
## 構築イメージ
![Drawing 2023-12-11 10.40.18.excalidraw.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/7691f838-ef89-536b-6096-887db01ec642.png)

実際にはsubnetやSGの情報を直接使うのではなくて、
terraformを実行した時の作成情報ファイル(tfstateファイル)をS3に保管するので、
それを参照して各情報を抜き取り、次のterraformで活用する感じ。

## 構築方法概要
〇ディレクトリツリー
![Drawing 2023-12-11 11.34.35.excalidraw.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/e9302186-46f1-f420-2ca5-d4e0e21a1055.png)

こんな感じに構築していると仮定すると、赤枠の部分を分解する。
variables.tfとかtfvarsファイルはそのまんまでも良いので、
modulesの実行管理部分のmodules.tfをとにかく分解する。

![Drawing 2023-12-11 11.34.36.excalidraw.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2737208/54c99ad8-7ab6-05dd-ea8c-2513cd7f8cfe.png)

上記みたいな感じにしておくと良い感じに思える。
実行時はstage1→stage2の2ステップになるが、それでも手動で作成するより遥かに楽。

## 構築方法（stage1、インフラ側）
実行するルートディレクトリ上にoutputs.tfを用意し、outputする情報を記載する。
tfstateファイルにはそもそも各リソースの情報が入ってはいるのだが、
それは外部にリソースを渡す前提で入っている情報では無い為、
別個に受け渡し用の情報を記載する必要がある。
**ここで書いた情報しか他のterraformは利用出来ない**。

``` hogeproject/environments/dev/stage1/outputs.tf
output vpc_id {
    value = module.vpc.vpc_id
}

output subnet_id {
    value = module.vpc.subnet_id
}

output sg_ec2_id {
    value = module.securitygroup.sg_ec2_id
}
```

## 構築方法（stage2、サーバー側）
実行するルートディレクトリ上にremote_state.tfを作成し、
どのtfstateファイルから情報を抜いてくるか指定をする。

``` hogeproject/environments/dev/stage2/remote_state.tf
data "terraform_remote_state" "data" {
  backend = "s3"

  config = {
    bucket = "terraform-hogefuga-bucket"
    key    = "tfstate/hogeproject_dev_stage1.tfstate"
    region = "ap-northeast-1"
  }
}
```

後はstage1のoutputs側で指定した値を利用出来る様になるので、
上手く指定しながら使う。
terraformのtfstateのバージョンによって以下の読み出し方が違うらしいので、
注意すること。これはtfstate version V2でのtfstateの読み方。

``` hogeproject/environments/dev/stage2/module_stage2.tf
~~

module "server" {
  source               = "../../../modules/server/ec2_instance/"
  subnet               = "${data.terraform_remote_state.data.outputs.subnet_id}"
  sg_ec2_id            = "${data.terraform_remote_state.data.outputs.sg_ec2_id}"
}

~~
```
