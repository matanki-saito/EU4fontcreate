import os
import re
import subprocess
from PIL import Image, ImageOps, ImageFilter,ImageEnhance

def invert(image):
    return image.point(lambda p: 255 - p)

def negeposi(name,ext):

    # 画像反転。組み込みのinvertではRGBAを処理できないために一度splitしている。
    im = Image.open('./out/' + name + ext).convert('RGBA');
    r, g, b, a = im.split();
    r, g, b = map(invert, (r, g, b))
    im_invert = Image.merge(im.mode, (r, g, b, a))

    # 白がきついので明るさを落とす
    enhancer = ImageEnhance.Brightness(im_invert)
    im_enh = enhancer.enhance(0.5)

    # ぼかし
    im_g = im_enh.filter(ImageFilter.GaussianBlur(radius=0.6))

    #上書き
    im_g.save('./out/'  + name + ".tga", quality=100)

def convertPngToDds(name,ext):
    #コマンド
    cmdList  =[
        '../1_tool/NvcompressFrontEnd/nvcompress/nvcompress.exe',
        '-rgb',
        './out/' + name + ext,
        './out/' + name + '.dds'
    ];

    #nvcompress実行
    subprocess.call(" ".join(cmdList));

def generateBMFont(name,ext,addSourceFile=False):
    #コマンド
    cmdList  =[
        '../1_tool/bmfont64.exe',
        '-c',"./bmfc/" + name + ext,
        '-o',"./out/" + name + ".fnt"
    ];

    #追加ファイルあり
    if(addSourceFile):
        cmdList.append('-t');
        cmdList.append(addSourceFile);
        
    #BFFont実行
    subprocess.call(" ".join(cmdList));

def readTextFile(name):
    f = open('./source/' + name + '.txt',"r",encoding='utf_8_sig')
    text = f.read();
    f.close();
    return text;

def main():
    sourceText = "";
    
    #sourceフォルダ内を走査
    files = os.listdir("./source");
    for file in files:
        #拡張子とファイル名を分離
        file_name, file_ext = os.path.splitext(file);

        #拡張子がtxt
        if(file_ext == ".txt"):
            sourceText = sourceText + readTextFile(file_name);

    validatedText="";
    #BMP外の文字がないかチェック
    for char in sourceText:
        if char == "¿":
            print("IGNORE: ¿");
            continue;
        if ord(char) > 0xFFFF:
            print("IGNORE: codePoint=" + str(hex(ord(char))));
            continue;
        validatedText += char;

    #source textを作成
    f = open('source.txt','w',encoding='utf_8_sig');
    f.write(validatedText);
    f.close();                

    #bmfcフォルダ内を走査
    files = os.listdir("./bmfc");
    for file in files:
        #拡張子とファイル名を分離
        file_name, file_ext = os.path.splitext(file);

        # フォント生成
        generateBMFont(file_name,file_ext,"source.txt");

    #outフォルダ内を走査
    files = os.listdir("./out");
    for file in files:
        #拡張子とファイル名を分離
        file_name, file_ext = os.path.splitext(file);

        if(file_ext == ".png"):
            #ネガポジ反転
            negeposi(file_name, file_ext);
        
            # 変換
            # convertPngToDds(file_name, file_ext);

if __name__ == "__main__":
    # execute only if run as a script
    main()
