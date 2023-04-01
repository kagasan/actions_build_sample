# actions_build_sample
外部からファイルをダウンロードして、それを素材にpagesをビルドしてオープンに公開するサンプル。
ダウンロード, ビルド, 公開までをactionsで実施する。

## ローカルで試す場合
```
# 外部ファイルをダウンロードする（外部とのやりとりのシミュレーション）
curl -o items.csv https://raw.githubusercontent.com/kagasan/sample_repository/main/sample.csv

# build
python3 build.py

# ローカルで動作確認
python3 -m http.server 8888

# ページ確認
http://[::]:8888/docs/
```

