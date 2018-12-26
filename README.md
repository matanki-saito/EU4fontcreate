# EU4fontcreate
## これはなに？
　Steam配信されているWindows版Europa Universalis IVの日本語化パッチの副産物です。パッチはこのプログラムを使って作成されたフォントのみを受け付けます。

## 環境
 - Windows10 以上
 - python 3以上をインストールしておく

## 使い方
 同梱しているbmfont64.exeを使用して、作成したいフォントのconfigurationファイル（.bmfc）をbmfcフォルダに保存してください。この時、含める文字は空にしてください。含めたい文字はsourceフォルダに任意の名前のBOM付きのUTF-8のtxtファイルに入れておきます。こちらで予めCP1252の追加文字と大体のSHIFT_JISの範囲の文字を入れたテキストを用意していますので、これ以外で必要な文字をtxtとして追加してください。

マップフォントを作る場合はhieroフォルダにあるREADMEを参照してください。

 準備が整ったら、generate.pyを実行します。outフォルダに生成されたフォントが入ります。

マップ用のフォントは上記とは別の方法で作られています。詳細はhieroフォルダにあるmemo.mdを参照してください。

## 使用フォントについて
 - [源ノ明朝](https://github.com/adobe-fonts/source-han-serif)
 - [源ノ角ゴシック](https://github.com/adobe-fonts/source-han-sans)

## 注意点

- CP1252の0x80から0x9Fまでに相当する文字（例えば€）はUCS2のコードポイントではなくて、CP1252のコードポイントとして作成されます。
- 0x100から0x1FFまでの文字は私用領域(0xE000)にシフトされたコードポイントになります。例えばλは3BBではなくて、0xE3BBのコードポイントになります。
- 0xE,0xFのコードポイントにはそれぞれ、日付用に"日"と"年"が割り振られます。

## ライセンス
　generate.pyはMITライセンス。bmfont64.exeはbmfontのソースライセンスに準拠。
