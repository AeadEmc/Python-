from selenium import webdriver
browser= webdriver.Chrome()
browser.get('http://quote.eastmoney.com/center/boardlist.html#boards2-90.BK0917')
element = browser.find_element_by_css_selector('#table_wrapper-table')

td_content = element.find_elements_by_tag_name("td")
list =[]
for td in td_content:
    list.append(td.text)
print(list)