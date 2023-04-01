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

## pagesの設定
- リポジトリ->Settings->Pages
- Source->GitHub Actions(Beta)->Static HTMLのConfigure
- static.ymlをリネーム「build_and_deploy.yml」
- ymlの内容を書き換え
```
name: build_and_deploy

# 実行開始条件
on:
  # mainにpushされた場合に実行
  push:
    branches: ["main"]

  # 手動実行したい場合
  workflow_dispatch:
  
  # 20分に一度実行する場合
  # schedule:
  #  - cron:  '*/20 * * * *'

# 権限設定
permissions:
  contents: read
  pages: write
  id-token: write

# ビルド進行の設定
concurrency:
  group: "pages"
  cancel-in-progress: false

# ワークフローのジョブ一覧
jobs:
  # ビルドジョブ
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Setup Pages
        uses: actions/configure-pages@v3
      - name: build
        run: |
          curl -o items.csv https://raw.githubusercontent.com/kagasan/sample_repository/main/sample.csv
          python3 build.py
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v1
        with:
          path: docs/ # 書き出す先のディレクトリ

  # デプロイジョブ
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2

```
- Start commitから保存
- mainにpushされるか手動実行でビルド&deployが実施される
- 公開先 : https://kagasan.github.io/actions_build_sample/

