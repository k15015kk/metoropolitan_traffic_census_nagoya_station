# 大都市交通センサス 1次ODデータ

## データ概要

1次ODデータは，複数のICカードカード媒体ごとの1日の改札機通過データを元に，入場/出場を1組にしたトリップデータである．

詳しいデータの詳細は [こちら](https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00600020&tstat=000001103355&cycle=0&tclass1=000001203341&tclass2=000001203350&tclass3val=0) から参照してください．

## データダウンロード方法

Terminalなどのコマンドラインアプリケーションにて，このディレクトリまでアクセスをします．その後，下記のコマンドを実行することで，このディレクトリに1次ODデータを全てダウンロードできます．なお，CSVファイルは `01.csv` ~ `12.csv` のように保存されます．

```zsh
sh download.sh
```

## 解析ファイル

サンプル解析ファイルとして `analyze.py` を用意しています．以下，内容はTBA．