# EU4fontcreate
# これはなに？
　Steam配信されているWindows版Europa Universalis IVの日本語化パッチの副産物です。パッチはこのプログラムを使って作成されたフォントのみを受け付けます。

# 環境
 - Windows10 以上
 - python 3以上をインストールしておく

# 使い方
 同梱のbmfont64.exeを使用して、作成したいフォントのconfigurationファイル（.bmfc）をbmfcフォルダに保存してください。この時文字は空にしてください。含めたい文字はsourceフォルダに任意の名前のutf-8のtxtファイルに入れておきます。準備が整ったら、generate.pyを実行します。outフォルダに生成されたフォントが入ります。

# ライセンス
　generate.pyはMITライセンス。bmfont64.exeはbmfontのソースライセンスに準拠。