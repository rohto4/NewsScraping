# -*- coding: utf-8 -*-
'''
Created on 2019/05/22

@author: Rohto
'''
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from abc import ABCMeta, abstractmethod

class NewsGetter(object):
    __metaclass__ = ABCMeta
    
    def __init__(self):
        self.options = Options()
#         self.options.add_argument('--headless')  # 起動時にブラウザを表示しない
        self.driver = webdriver.Chrome('chromedriver.exe', options=self.options)
    
    @abstractmethod
    def collect(self):
        '''
        取得処理
        '''
        
    @abstractmethod
    def login(self):
        '''
        ログイン
        '''
        
    def notice(self):
        '''
        通知処理
        '''
        
    
    @staticmethod
    def byTechfeed(set):
        return TechfeedGetter(set)
    
#     @staticmethod
#     def byITmedia(search_set):
#         return ITmediaGetter(search_set)
#         
    
class TechfeedGetter(NewsGetter):
    def __init__(self, set):
        super(TechfeedGetter, self).__init__()
        self.set = set
        self.address = 'rohto111117@gmail.com'
        self.password = 'takehiro1290'
        self.login()
    
    # override         
    def collect(self):
        self.driver.get('file:///C:/work/IDE/Git/20_work/git/NewsScraping/test/test_site.html')
#         self.driver.get('https://techfeed.io/main/realtime/000000000000000000000008')
        self.driver.implicitly_wait(3)
        html = self.driver.page_source.encode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        
        self.driver.implicitly_wait(3)
        # お知らせがある場合完了をクリック
        popup = soup.find('div', class_='popover-content')
        print(popup)
        if None != popup:
            popup.findAll('ion-button').click()
 #             soup.find_element_by_class_name('button')
        
        # 記事数分処理
        news = []
        i = 0
        for x in soup.findAll('div', class_='entry-container'):
            news[i]['entry_title'] = x.find('h1', class_='entry-title-text')
            news[i]['rank_type'] = x.find('span', class_='rank__type')
            news[i]['rank_text'] = x.find('span', class_='rank__text')
            news[i]['ion_label_all'] = x.findAll('span', class_='ion-label')
            print(news[i]['entry_title'])
            print(news[i]['rank_type'])
            print(news[i]['rank_text'])
            print(news[i]['ion_label_all'])
            i += 1
        
        for text in news:
            print('entry_title:' + text['entry_title'])
            print('rank ' + text['rank_type'] + ' ' + ' / '.join(text['ion_label_all']))
    
    # override
    def login(self):
        # ログインページにアクセス
        self.driver.get('https://techfeed.io/main/global/anonymous/login')
        self.driver.implicitly_wait(1)
        html = self.driver.page_source.encode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        
        # 必要情報を入力
        self.driver.find_element_by_name('ion-input-0').send_keys(self.address)
        self.driver.find_element_by_name('ion-input-1').send_keys(self.password)
        # ログインボタンをクリック
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_class_name('login-button')
        
        
     
# class ITmediaGetter(NewsGetter)
#     __init__():
#         
#     
#     @override
#     def collect():
#         
#     
#     @override
#     def login():
#         

if __name__ == '__main__':
    # 絞込み条件設定
    set = {
        'URL': ['https://techfeed.io/main/realtime/000000000000000000000002',
                'https://techfeed.io/main/realtime/000000000000000000000004',
                'https://techfeed.io/main/realtime/000000000000000000000008'],
        'ion-label': ['JavaScript','Java', 'Python', 'GitHub'],
        'entry-title-text': '',
        'keyword': ''
    }
    getter = NewsGetter.byTechfeed(set)
    getter.collect()
