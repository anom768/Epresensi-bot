from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = input("Masukkan username: ")
password = input("Masukkan password: ")

web = webdriver.Chrome()

web.get("https://student.amikompurwokerto.ac.id/auth")
web.find_element_by_xpath('//*[@id="exampleInputEmail1"]').send_keys(username)
web.find_element_by_xpath('//*[@id="exampleInputPassword1"]').send_keys(password)
web.find_element_by_css_selector('#login-form > div > div:nth-child(6) > button').click()
time.sleep(5)
web.get("https://student.amikompurwokerto.ac.id/presensi")

web.find_element_by_css_selector('#thn_akademik').click()
web.find_element_by_css_selector('#thn_akademik').send_keys(Keys.ENTER)
time.sleep(1)
web.find_element_by_id('semester').click()
web.find_element_by_id('semester').send_keys(Keys.ARROW_DOWN)
web.find_element_by_id('semester').send_keys(Keys.ENTER)
web.find_element_by_id('semester').click()
web.find_element_by_id('semester').send_keys(Keys.ENTER)

time.sleep(1)
web.find_element_by_css_selector('#makul').click()
web.find_element_by_xpath('//*[@id="makul"]').send_keys(Keys.ENTER)
web.find_element_by_css_selector('#makul').click()
web.find_element_by_xpath('//*[@id="makul"]').send_keys(Keys.ENTER)
time.sleep(2)

def navigasi_makul():
    web.find_element_by_css_selector('#makul').click()
    web.find_element_by_xpath('//*[@id="makul"]').send_keys(Keys.ARROW_DOWN)
    web.find_element_by_xpath('//*[@id="makul"]').send_keys(Keys.ENTER)
    web.find_element_by_css_selector('#makul').click()
    web.find_element_by_xpath('//*[@id="makul"]').send_keys(Keys.ENTER)

def teori():
    elemen = ['kesesuaian_perkuliahan1','kesesuaian_materi1','penilaianmhs4']
    time.sleep(2)
    for i in elemen:
        web.find_element_by_id(i).click()

def praktek():
    time.sleep(2)
    teori()
    elemen = ['0','1','2','3','4',['label']]
    for i in elemen[0:3]:
        for j in elemen[5]:
            web.find_element_by_id('ui-id-asdos-'+str(i)+'-'+str(j)).click()
            time.sleep(1)
            for k in elemen[1:5]:
                try:
                    web.find_element_by_id('asdospenilaian_'+str(i)+'_'+str(k)).click()
                except:
                    pass

def scan():
    for i in range(1,3):
        for j in range(1,29):
            try:
                tabel = '/html/body/div/div[6]/div/div/div[2]/div/div/div/div/div/table['+str(i)+']/tbody/tr['+str(j)+']/td[3]/a'
                web.find_element_by_xpath(tabel).click()
                if i == 1:
                    teori()
                    web.find_element_by_id('btnsimpan').click()
                    time.sleep(2)
                else:
                    praktek()
                    web.find_element_by_id('btnsimpan').click()
                    time.sleep(2)
            except:
                pass

if __name__ == '__main__':
    for i in range(1,9):
        scan()
        if i == 8:
            web.quit()
            quit()
        navigasi_makul()
        time.sleep(2)