import os
import subprocess


def generate_bm_font(name, ext, add_source_file):
    # コマンド
    cmd_list = [
        '../1_tool/bmfont64.exe',
        '-c', "./bmfc/" + name + ext,
        '-o', "./out/" + name + ".fnt"
    ]

    # 追加ファイルあり
    if add_source_file:
        cmd_list.append('-t')
        cmd_list.append(add_source_file)

    # BFFont実行
    subprocess.call(" ".join(cmd_list))


def read_text_file(name):
    f = open('./source/' + name + '.txt', "r", encoding='utf_8_sig')
    text = f.read()
    f.close()
    return text


def main():
    source_text = ""

    # sourceフォルダ内を走査
    files = os.listdir("./source")
    for file in files:
        # 拡張子とファイル名を分離
        file_name, file_ext = os.path.splitext(file)

        # 拡張子がtxt
        if file_ext == ".txt":
            source_text = source_text + read_text_file(file_name)

    # source textを作成
    f = open('source.txt', 'w', encoding='utf_8_sig')

    validated_text = ""
    # BMP外の文字がないかチェック
    for char in source_text:
        if char == "¿":
            print("IGNORE: ¿")
            continue
        if ord(char) > 0xFFFF:
            print("IGNORE: codePoint=" + str(hex(ord(char))))
            continue
        validated_text += char

    f.write(validated_text)
    f.close()

    # bmfcフォルダ内を走査
    files = os.listdir("./bmfc")
    for file in files:
        # 拡張子とファイル名を分離
        file_name, file_ext = os.path.splitext(file)

        # 拡張子がbmfcの時のみフォントを生成
        if file_ext == ".bmfc":
            generate_bm_font(file_name, file_ext, "source.txt")


if __name__ == "__main__":
    # execute only if run as a script
    main()
