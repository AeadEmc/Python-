from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import requests
from bs4 import BeautifulSoup
import find_data_link
browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
browser.maximize_window()  # 最大化窗口,可以选择设置




def index_page(page):
        try:
            browser.get('http://quote.eastmoney.com/center/boardlist.html#boards2-90.BK0917')
            print('正在爬取第：%s页'%page)
            if page == 1:
                element = browser.find_element_by_css_selector('#table_wrapper-table')
                td_content = element.find_elements_by_tag_name("td")
                links = element.find_elements_by_css_selector('#table_wrapper-table > tbody > tr> td.listview-col-Links > a:nth-child(3)')
                lst_link = []
                for link in links:
                    url = link.get_attribute('href')
                    url=find_data_link.findlink(url)
                    lst_link.append(url)
                for td in td_content:
                    lst_link.append(td.text)
                print(lst_link)
            if page > 1:
               input = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="main-table_paginate"]/input')))
               input.click()
               input.clear()
               input.send_keys(page)
               submit = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="main-table_paginate"]/a[3]')))
               submit.click()
               time.sleep(1)# 必要等待页面加载
               element = browser.find_element_by_css_selector('#table_wrapper-table')  #爬虫主体
               td_content = element.find_elements_by_tag_name("td")
               links = element.find_elements_by_css_selector('#table_wrapper-table > tbody > tr> td.listview-col-Links > a:nth-child(3)')
               lst_link=[]
               for link in links:
                   url = link.get_attribute('href')
                   url = find_data_link.findlink(url)
                   lst_link.append(url)
               for td in td_content:
                   lst_link.append(td.text)
               print(lst_link)
        except Exception:
            print("wrong")
            return list
def main():
    for page in range(1,8):
        list=index_page(page)
    return list
if __name__=='__main__':
     list=main()




