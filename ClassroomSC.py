import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#driver = webdriver.Chrome()

wantTime=time.ctime().split(' ')[3]


def job():
    driver=webdriver.Chrome('C:\chromdriver/chromedriver.exe')
    action = ActionChains(driver)
    driver.get("https://classroom.google.com/u/0/h")
    #구글 로그인
    driver.find_element_by_id('identifierId').send_keys('your email')
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
    driver.implicitly_wait(5)
    driver.find_element_by_name("password").send_keys('your password')
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()
    driver.implicitly_wait(5)

    #과목의 타이틀 클릭
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[4]/div/div[1]/div/ol/li[2]/div[1]/div[3]/h2/a[2]').click()
    driver.implicitly_wait(5)

    #meet링크 클릭
    move_to_element(driver.find_element_by_css_selector('.onkcGd ZmqAt')).click()
    driver.implicitly_wait(5)
    move_to_element(driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[4]/div[2]/div[1]/div/div[2]/div[2]/span')).click()
    driver.implicitly_wait(5)

    #채팅창에 출석 입력후 전송
    driver.find_element_by_css_selector('.KHxj8b tL9Q4c').send_keys('출석')
    driver.find_element_by_css_selector('.CEJND cIGbvc NMm5M hhikbc').click()

    
schedule.every().day.at("10:24").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
