import MySQLdb
import item as item
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
def getdata(url):
    browser= webdriver.Chrome()
    browser.get(url)
    wait = WebDriverWait(browser, 10)
    # submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[(@id = "xjllb_ul")]//li')))
    # submit.click()
    # time.sleep(1)  # 必要等待页面加载
    element = browser.find_element_by_xpath('//*[@id="report_zyzb"]')#先找到网页中的表格
    td_content = element.find_elements_by_xpath('//*[@id="report_zyzb"]/table/tbody/tr[10]')#在表格中进行筛选
    list =[]   #创建列表存储数据

    for td in td_content:
        list.append(td.text)    #将所有数据放在一个列表中
    list = list[0].split()
    a = browser.find_element_by_xpath('//*[@id="report_zyzb"]')
    b = a.find_elements_by_xpath('//*[@id="report_zcfzb"]/tbody/tr[81]')
    lst= []
    for td in b:
        lst.append(td.text)
    lst=lst[0].split()
    list=list+lst
    name = browser.find_element_by_css_selector('#hq_1')
    code = browser.find_element_by_css_selector(
        'body > div.main > div:nth-child(1) > div:nth-child(9) > div > div.scklox > div > p.key > a')
    syl = browser.find_element_by_css_selector("#hq_13")
    list.append(name.text)
    list.append(code.text)
    list.append(syl.text)
    print(list)
    name=list[-3]
    code=list[-2]
    syl = round(float(list[-1]),2)
    print(syl)
    zsra=str(list[1]).replace("亿",'')
    zsra= zsra.replace("万", '')
    zsra=round(float(zsra),2)
    print(zsra)
    zsrb=str(list[2]).replace("亿",'')
    zsrb = zsrb.replace("万", '')
    zsrb=round(float(zsrb),2)
    print(zsrb)
    zsrc=str(list[3]).replace("亿",'')
    zsrc = zsrc.replace("万", '')
    zsrc=round(float(zsrc),2)

    zfa=str(list[12]).replace("亿",'')
    zfa = zfa.replace("万", '')
    zfa=round(float(zfa),2)

    zfb=str(list[13]).replace("亿",'')
    zfb=zfb.replace("万",'')
    zfb=round(float(zfb),2)

    zfc=str(list[14]).replace("亿",'')
    zfc = zfc.replace("万", '')
    zfc=round(float(zfc),2)

    conn=MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='112320',
        db='gp',
        use_unicode=True,
        charset="utf8"
    )
    cur=conn.cursor()
    sql="insert into gpdata VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s');"%(name,code,zsra,zsrb,zsrc,zfa,zfb,zfc,syl)

    try:
        #cur.execute(sql,(name,code,zsra,zsrb,zsrc,zfa,zfb,zfc))
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print('wrong:%s'%e)
        conn.rollback()

    conn.close()




