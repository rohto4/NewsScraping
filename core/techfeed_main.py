# -*- coding: utf-8 -*-
'''
Created on 2019/05/08

@author: Rohto
'''
import requests
import bs4
import csv
import sys

# ホットエントリページの取得、解析
def main():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"} #User-Agentは自身のブラウザとOSを設定する
    
    res = requests.get("https://techfeed.io/main/realtime/000000000000000000000008", timeout=10, headers=headers)
    
    print(res.text)
    sys.exit()
    bs_res = bs4.BeautifulSoup(res.text, "lxml")
    
    print()
    # 表示用領域
    techfeed_pg = []
    # articleタグ内の要素をすべて取得
    for x in bs_res.findAll("article", attrs={"class":"type-article"}):
        # タイトル
        title_text_tag = x.find("h1", attrs={"class":"entry-title-text"})
        # カテゴリ
        ion_label_tag = x.findAll("span", attrs={"class":"ion-label"})
        # 複数取得できた場合は結合
        print("aa"+type(ion_label_tag))
        sys.exit()
        if isinstance(ion_label_tag, list):
            
            ion_label_tag = ' / '.join(ion_label_tag)
        # ランク
        rank_type_label = x.find("span", attrs={"class":"rank__type"})
        # ランクテキスト
        rank_text_label = x.find("span", attrs={"class":"rank__text"})
    
        if ion_label_tag is not None:
#             techfeed_pg.append((title_text_tag.text, a_tag.attrs["title"], a_tag.attrs["href"]))
            print('a')

    print(techfeed_pg)
    # 確認用に表示
    # x[0] : entry-title-text
    # x[1] : ion-label配列[]
    # x[2] : rank__type rank__text
    # x[3] : entry-content-main
#     for x in techfeed_pg:
#         print('{}\n{} / {}   [{}]\n{}'.format(x[0], x[1], x[2], x[3], x[4]))
    
    # csvに出力
#     f = open('techfeed.csv', 'w')
    f = open('techfeed.csv', 'w', encoding='CP932', errors='ignore') #windows環境用、エンコードエラー回避
    
    writer = csv.writer(f, lineterminator='\n')
    
    for x in techfeed_pg:
        writer.writerow(x)
    
    f.close()

    

if __name__ == '__main__':
    main()
