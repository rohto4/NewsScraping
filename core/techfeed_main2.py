# -*- coding: utf-8 -*-
'''
Created on 2019/05/09

@author: Rohto
'''
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    options = Options()
    # ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
    options.add_argument('--headless')
    # 起動
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    # アクセス
    driver.get('https://techfeed.io/main/realtime/000000000000000000000008')
    # utf-8で取得
    html = driver.page_source.encode('utf-8')
    # beautifulSoupで扱えるようにパース
    soup = BeautifulSoup(html, 'html.parser')
    # 要素の取得
    print(soup.title)
    
    for x in soup.findAll('div', class_='entry-container'):
        entry_title = x.find('h1', class_='entry-title-text')
        rank_type = x.find('span', class_='rank__type')
        rank_text = x.find('span', class_='rank__text')
        ion_label_all = x.findAll('span', class_='ion-label')
        print(entry_title)
        print(rank_type)
        print(rank_text)
        print(ion_label_all)
        
if __name__ == '__main__':
    main()