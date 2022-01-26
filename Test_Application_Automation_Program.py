# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
def click_button(xpath, waiting_time):
    driver.find_element_by_xpath(xpath).click()  # 요소 선택하여 클릭   
    time.sleep(waiting_time)

def input_data(xpath, input_value, waiting_time):
    driver.find_element_by_xpath(xpath).send_keys(input_value) # id 입력창에 id 입력
    time.sleep(waiting_time)

def find_button(kind_array, find_value):
    cnt = 0
    for select in kind_array:
        #if select.option == find_value:
        if cnt == 2:
            print("--------------------------------")
            return select
        cnt = cnt + 1
        break;

driver=webdriver.Chrome('/Users/hoyonglee/Downloads/makro/chromedriver') #크롬 드라이버
driver.get('http://www.q-net.or.kr/rcv002.do?id=rcv00208&gSite=Q&gId=03&rcvPFlag=Y&gTitle=') #접속할 url
time.sleep(3.0)

input_data('//input[@id="mem_id"]', '여기에 : q-net아이디를 입력하세요!!', 0.3)
input_data('//input[@id="mem_pswd"]', '여기에 : q-net 비밀번호를 입력하세요!!', 0.3)
click_button('//*[@class="btn_login"]', 1) #로그인 버튼 클릭
click_button('//*[@id="RCV002_01"]/a', 1) #원서접수신청  버튼 클릭
click_button('//*[@id="content"]/div[3]/div[2]/div/table/tbody/tr[1]/td[3]/button/span', 1) #원서접수신청  버튼 클릭
select = Select(driver.find_element_by_id('sel_01'))
select.select_by_visible_text('정보처리기사')

click_button('//*[@id="infoChk"]', 1) # 동의 체크박스
click_button('//*[@id="content"]/div[4]/a[2]', 1) # 다음버튼

result = driver.switch_to_alert()
result.accept() # Message: unexpected alert open: 을해결하기 위해 사용.
time.sleep(2)

click_button('//*[@id="content"]/div[7]/div[4]/button[4]', 1) # 장소및결제하기
click_button('//*[@id="content"]/div[2]/form/div[2]/a', 1) # 다음버튼

while(1):
    select2 = Select(driver.find_element_by_id('sel_zone'))
    select2.select_by_visible_text('서울특별시')
    click_button('//*[@id="content"]/div[2]/form[1]/div/span[6]/button', 1) # 장소및결제하기
    break
#print("--------------------------end")
#def autoClick():
#    btns= driver.find_elements_by_xpath('//*[@id="sel_zone"]/div[*]')
#    for btn in btns:
#        if btn.text == "서울특별시":
#            btn.click()
#            print("서울특별시 clicked!")
#            break
#    time.sleep(2.1)
#autoClick()


#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#
#driver = webdriver.Chrome(executable_path="/Users/hoyonglee/Downloads/makro/chromedriver")
#url = 'https://cls4.edunet.net/cyber/cm/mcom/pmco000b00.do'
#driver.get(url)
#
#driver.find_elements_by_css_selector('a.btn_login')[1].click()
#driver.find_elements_by_css_selector('dd.dd_2')[0].click()
#driver.find_element_by_id('login_id').send_keys('id')
#driver.find_element_by_id('password').send_keys('password!')
#driver.find_element_by_id('password').send_keys(Keys.ENTER)
