'''
Created on 2019/05/08

@author: Rohto
'''
import requests
import bs4
import csv

# �z�b�g�G���g���y�[�W�̎擾�A���
def main():
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.84 Safari/537.36"} #User-Agent�͎��g�̃u���E�U��OS��ݒ肷��
    
    res = requests.get("https://techfeed.io/main/realtime/000000000000000000000008", timeout=10, headers=headers)
    
    bs_res = bs4.BeautifulSoup(res.text, "lxml")
    
    # �͂ău���ƃ^�C�g���̎擾
    techfeed_pg = []
    for x in bs_res.findAll("div", attrs={"class":"type-article"}):
        a_tag = x.find("a", attrs={"class":"js-keyboard-openable"})
        hatebu_num = x.find("a", attrs={"class":"js-keyboard-entry-page-openable"})
    
        if a_tag is not None:
            techfeed_pg.append((hatebu_num.find("span").text, a_tag.attrs["title"], a_tag.attrs["href"]))
    
    # �͂ău���Ń\�[�g
    techfeed_pg = sorted(techfeed_pg, key=lambda x:int(x[0]), reverse=True)
    
    # �m�F�p�ɕ\��
    # x[0] : title
    # x[1] : 
    # x[2] :
    # x[3] :
    # x[4] :
    for x in techfeed_pg:
        print('{} || {} \n {}'.format(x[0], x[1], x[2]))
    
    # csv�ɏo��
#     f = open('techfeed.csv', 'w')
    f = open('techfeed.csv', 'w', encoding='CP932', errors='ignore') #windows���p�A�G���R�[�h�G���[���
    
    writer = csv.writer(f, lineterminator='\n')
    
    for x in techfeed_pg:
        writer.writerow(x)
    
    f.close()

    

if __name__ == '__main__':
    main()
