'''
Created on 2019/05/23

@author: Rohto
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
 
try :
    opt = Options()
 
    # Headless���[�h��L���ɂ���
    # ������True�ɐݒ肷��ƃu���E�U���N�����������s�ł��܂�
    opt.set_headless(False)
    # Chrome���N������@�@
    driver = webdriver.Chrome(chrome_options=opt)
    # �w�肵���v�f��������܂ł̑҂����Ԃ�ݒ�i20�b�j
    driver.implicitly_wait(20)
    
    # Garmin Connect�̃y�[�W��\��
    driver.get("https://connect.garmin.com/ja-JP/signin")
 
    # iframe����DOM�𑀍�ł���悤�ɂ���
    elm = driver.find_element_by_id("gauth-widget-frame-gauth-widget")
    driver.switch_to_frame(elm)
 
    # ID�̓��͗v�f���擾
    elm = driver.find_element_by_id("username")
    # ID�����
    elm.send_keys([ID���w��])
 
    # �p�X���[�h�̓��͗v�f���擾
    elm = driver.find_element_by_id("password")
    # �p�X���[�h�����
    elm.send_keys([�p�X���[�h���w��])
 
    # �T�C���C���{�^�����擾
    elm = driver.find_element_by_id("login-btn-signin")
    # �T�C���C���{�^�����N���b�N
    elm.click()
 
    # ������ʂ������Ă��܂��̂Ŋm�F���邽�߂�5�b�X���[�v������
    sleep(5)
except Exception as ex :
    # ��O����
    print(ex)
finally:
    # webdriver�̃C���X�^���X����������Ă���ꍇ�AChrome���I��
    if "driver" in vars() and driver is not None :
