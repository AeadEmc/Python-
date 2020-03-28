from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import find_data

def findlink(url):
    browser = webdriver.Chrome()
    browser.maximize_window()  # 最大化窗口,可以选择设置
    wait = WebDriverWait(browser, 10)
    browser.get(url)
    links = browser.find_elements_by_css_selector('#m_cwzy > div.cateday > ul > li:nth-child(2) > a')
    lst_link = []
    for link in links:
        url = link.get_attribute('href')
        lst_link.append(url)
    print(lst_link)
    find_data.getdata(lst_link[0])
    browser.close()
# findlink('http://data.eastmoney.com/stockdata/300458.html')


