# Learn CDK in SageMaker Studio Lab

[SageMaker Studio Lab](https://studiolab.sagemaker.aws/users/ttaakkaa)で[CDK](https://aws.amazon.com/jp/cdk/)を動かすサンプルです。LambdaによるシンプルなAPI(API Gateway)を構築します。`aws-cdk-examples`の[api-cors-lambda](https://github.com/aws-samples/aws-cdk-examples/tree/master/python/api-cors-lambda)をベースにしています。

Studio LabはCDKのハンズオンに適しています。

* ハンズオン参加者の環境をそろえることができる。
* 無料。
* ターミナルが利用できる。

例えばCloud9を使うハンズオンだと、インスタンスの起動/停止が必要で起動中はもちろん料金がかかります。Studio Labであれば、参加者の環境を共通化しつつ料金が無料で済みます。また、ターミナルが利用できるためcdkのようなコマンドラインベースで進めるハンズオンも実施することができます。

## Studio Labの準備

[Getting started with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)に沿って進めます。次の手順で環境を構築してください。

1. Prerequisites: AWS上でCDKに使用するユーザーを作成し、`aws configure`で設定します。
2. Install the AWS CDK: `conda install nodejs`を実行したのち、`npm install -g aws-cdk`で`aws-cdk`をインストールします。
3. Bootstrapping: `cdk bootstrap aws://ACCOUNT-NUMBER/REGION`でCDK用のS3バケットを作成します。

Studio LabではCondaで環境を構築します。次のコマンドを実行してください。

```
conda env create -f environment.yml
```

以後、`cdk deploy`/`cdk destroy`で構築/削除を行います。

新規にCDKのアプリケーションを開始する時は、次のコマンドを新しいフォルダで実施してください。

```
cdk init app --language python
```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
