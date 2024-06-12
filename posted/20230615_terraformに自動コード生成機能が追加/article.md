# terraformのv1.5.0リリース
https://www.hashicorp.com/blog/terraform-1-5-brings-config-driven-import-and-checks

インポート機能の強化が肝。うれしい。

# terraformのインポート機能
これまでもインポート機能はあったが、既存のリソースを
terraformの管理下に置く(******.tfstateファイルに記載する）だけだった。
それをベースに書く事は可能だけれど。

今回のアップデートから、**tfファイルを自動生成**する事が可能になった。
これで特にterraformの知識が無くても、リソースさえ適切に作れてしまえば
リソース作成→terraform作成という流れでterraformコードを記載出来る。
勿論terraform内での構造は調整する必要はあるが。
Excel VBA書く時にめんどい部分をExcelのマクロを記録して、
それを元にコード書いてしまう様なイメージが近いかも。

# やり方
## 限界構成
これだけ。
```
  importer
    | -- generated(directory)
    | -- provider.tf
    | -- import.tf
```


### 中身
import.tfに対象のリソースのidと作成時のリソースを記載する。
何のリソースを取り込むかの指定をする必要があるので、
そこだけ事前に調べる必要がある。
下記はEC2インスタンスを指定した例。

``` import.tf
import {
  id = "i-xxxxxxxx" # リソースの識別子
  to = aws_instance.ec2          # import対象
}
```

# 実例
作成済EC2インスタンスのインスタンスIDをコンソールから拾う。
これがimport.tfのidに相当。

また、ステートマネージャのterraform上でのリソース記載は
**aws_instance**になるので、toにはこれを記載する。

実行は、importerディレクトリに移動した上で以下。
```
$ terraform init
$ terraform plan -generate-config-out=generated/instance.tf
```

上手く実行されると、実行時に指定された名称でtfファイルが出来る。
不必要なパラメータを外したり、変数にしたりして調整するとgood。
terraformの公式説明が分かり辛いので、この機能は便利だと思う。


``` generated/instance.tf
# __generated__ by Terraform
# Please review these resources and move them into your main configuration files.
resource "aws_instance" "ec2" {
  ami                                  = "ami-xxxxxxxx"
  associate_public_ip_address          = true
  availability_zone                    = "ap-northeast-1a"
  cpu_core_count                       = 1
  cpu_threads_per_core                 = 1
  disable_api_stop                     = false
  disable_api_termination              = false
  ....
```
