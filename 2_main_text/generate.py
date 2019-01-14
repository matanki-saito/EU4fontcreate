import os
import re
import subprocess

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

    #source textを作成
    f = open('source.txt','w',encoding='utf_8_sig');
    f.write(sourceText);
    f.close();                

    #bmfcフォルダ内を走査
    files = os.listdir("./bmfc");
    for file in files:
        #拡張子とファイル名を分離
        file_name, file_ext = os.path.splitext(file);

        #拡張子がbmfcの時のみフォントを生成
        if(file_ext == ".bmfc"):
            generateBMFont(file_name,file_ext,"source.txt");

if __name__ == "__main__":
    # execute only if run as a script
    main()
