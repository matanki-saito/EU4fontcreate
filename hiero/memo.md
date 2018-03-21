#Map用フォント

##準備
 - Javaが起動する環境。JREをインストールすればOK。
 - この[リンク](https://github.com/libgdx/libgdx/wiki/Hiero)からHieroをダウンロードしてzipを解凍しておく。
 - この[リンク](http://ch.nicovideo.jp/sevrunear/blomaga/ar539518)からNvcompressFrontEndをダウンロードしてzip解凍しておく。

##フォントfntとテクスチャpng画像の生成
Hieroを解答したフォルダのアドレスバーに「cmd」と入力して、コマンドプロンプトを開き、下記のコマンドをペーストして、Enterを押す。

```java -cp gdx.jar;gdx-natives.jar;gdx-backend-lwjgl.jar;gdx-backend-lwjgl-natives.jar;extensions\gdx-freetype\gdx-freetype.jar;extensions\gdx-freetype\gdx-freetype-natives.jar;extensions\gdx-tools\gdx-tools.jar com.badlogic.gdx.tools.hiero.Hiero
```

起動したHieroからYuMincho60bold.hieroを読み込む。
![img](2018-03-21_16h44_47.png)

メニュー＞File＞Save BMFontで、ファイルを書き出す用に指示。時間はかかるが指定した場所にfntファイルとpngファイルが出来上がるのを待つ。

##テクスチャpng画像をddsに変換する
NvcompressFrontEndを起動して、規定のフォーマットをRGBAにする。

![img2](2018-03-21_16h48_12.png)

pngファイルをD&Dして、変換ボタンを押す。一瞬でddsに変換される。

