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
    driver.get('https://techfeed.io/main/realtime/00000000000000000000000')
    # utf-8で取得
    html = driver.page_source.encode('utf-8')
    # beautifulSoupで扱えるようにパース
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.find_all(True):
        print(tag.name)
    
    # 要素の取得
    print(soup.title)
    

if __name__ == '__main__':
    main()