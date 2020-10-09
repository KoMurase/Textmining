import re 
import os 

def remove_words(text):
    #本文の説明の削除
    text = text.split('-------------------------------------------------------')[2]
    #ルビの削除
    text = re.sub(r'《[^》]+》','',text)
    #改行コードの削除
    text = re.sub(r'\n','',text)
    #句読点の削除
    text = re.sub(r'。|、','',text)
    #空行の削除
    text = re.sub(r'^\n', '', text)
    #空白の削除
    text = text.replace('　','')
    #URLを除去する
    text = re.sub(
      r'(http|https)://([-\w]+\.)+[-\w]+(/[-\w./?%&=]*)?', 
      "",
      text)

    return text 


def read_text(path):

    f = open(path, 'r')
    #data_list = f.readlines() #1行ずつのリスト
    data = f.read()
    f.close() 
    return data

def write_text(data, title):
    file_name = r"C:\Users\mkou0\Desktop\TM\after\太宰治_{}.txt".format(title)
     
    file = open(file_name, "w", encoding="utf_8")
    file.write(data)
    file.close() 
    print("{}を書き込みました".format(title))

def pipeline(path):
    data = read_text(path)
    data = remove_words(data)
    title = os.path.split(path)[1].replace('.txt', '')
    write_text(data, title)


if __name__ == '__main__':
    #path : 処理前のテキストの格納先
    root_name = r"C:\Users\mkou0\Desktop\TM\before"

    files_list = os.listdir(root_name)
    print(files_list)

    for file_name in files_list:
        path = os.path.join(root_name, file_name)
        pipeline(path)
        

    print("ALL DONE")
"""
    data = read_text(path)
    #print(data)
    #print('-'*80)
    data = remove_words(data)
    #print(data)
    title = os.path.split(path)[1].replace('.txt', '')
    print(title)
    write_text(data, title)
"""