'''
Created on 2019/05/23

@author: Rohto
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
 
try :
    opt = Options()
 
    # Headlessモードを有効にする
    # 引数をTrueに設定するとブラウザを起動させず実行できます
    opt.set_headless(False)
    # Chromeを起動する　　
    driver = webdriver.Chrome(chrome_options=opt)
    # 指定した要素が見つかるまでの待ち時間を設定（20秒）
    driver.implicitly_wait(20)
    
    # Garmin Connectのページを表示
    driver.get("https://connect.garmin.com/ja-JP/signin")
 
    # iframe内のDOMを操作できるようにする
    elm = driver.find_element_by_id("gauth-widget-frame-gauth-widget")
    driver.switch_to_frame(elm)
 
    # IDの入力要素を取得
    elm = driver.find_element_by_id("username")
    # IDを入力
    elm.send_keys([IDを指定])
 
    # パスワードの入力要素を取得
    elm = driver.find_element_by_id("password")
    # パスワードを入力
    elm.send_keys([パスワードを指定])
 
    # サインインボタンを取得
    elm = driver.find_element_by_id("login-btn-signin")
    # サインインボタンをクリック
    elm.click()
 
    # すぐ画面が消えてしまうので確認するために5秒スリープさせる
    sleep(5)
except Exception as ex :
    # 例外処理
    print(ex)
finally:
    # webdriverのインスタンスが生成されている場合、Chromeを終了
    if "driver" in vars() and driver is not None :
