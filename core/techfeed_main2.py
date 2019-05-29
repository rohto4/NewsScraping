# -*- coding: utf-8 -*-
'''
Created on 2019/05/09

@author: Rohto
'''
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from abc import ABCMeta, abstractmethod
# from xlwt import Workbook

class NewsGetter(object):
    __metaclass__ = ABCMeta
    
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--headless')  # 起動時にブラウザを表示しない
       
    @abstractmethod
    def login(self):
        '''
        ログインして検索設定値を適用する
        '''
        
    def collect(self):
        # 起動
        self.driver.implicitly_wait(3)
        # アクセス
        self.driver = webdriver.Chrome('chromedriver.exe', options=self.options)
        self.driver.get('https://techfeed.io/main/realtime/000000000000000000000008')
        # utf-8で取得
        html = self.driver.page_source.encode('utf-8')
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
            print(' / '.join(ion_label_all))
    
    def notice(self):
        '''
        結果を通知
        '''
    @staticmethod
    def byTechfeed():
        return TechfeedGetter(search_set)
    
    @staticmethod
    def byITmedia():
        return ITmediaGetter(search_set)
        
class TechfeedGetter(NewsGetter):
    def __init__(self, set):
        # Techfeed特有の設定
        self.set = set
    
    def collect(self):
        
    
    def login(self):
        
        
class ITmediaGetter(NewsGetter):
    def __init__(self, set):
        # ITmedia特有の設定
        self.set = set
        
if __name__ == '__main__':
    # techfeedからデータを取得
    search_set = []
    getter = NewsGetter.byTechfeed(search_set)
        