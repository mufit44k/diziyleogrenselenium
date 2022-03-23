from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import requests
import pandas
anal = []
driver = webdriver.Chrome()
driver.get("https://diziyleogren.com/dizi/ingilizce/mr-robot-kelimeler-ve-anlamlari")
driver.maximize_window()
sleep(10)
next = driver.find_element_by_xpath("//*[@id='next']")
next.click()
sleep(2)

next = driver.find_element_by_xpath("//*[@id='pick-episode']/option[4]")
next.click()
sleep(10)
liste = driver.find_element_by_xpath("//*[@id='slider-range-min']/span")
# ActionChains(driver).click_and_hold(liste).drag_and_drop_by_offset(liste, -25, 0)
ActionChains(driver).click_and_hold(liste).pause(2).move_by_offset(-100, 0).release().perform()
sleep(2)
ActionChains(driver).click_and_hold(liste).pause(2).move_by_offset(-100, 0).release().perform()
sleep(2)
ActionChains(driver).click_and_hold(liste).pause(2).move_by_offset(-125, 0).release().perform()
sleep(2)
ActionChains(driver).click_and_hold(liste).pause(2).move_by_offset(-150, 0).release().perform()
sleep(5)
listee = driver.find_element_by_xpath("//*[@id='tbodyWord']")
liste2 = listee.find_elements_by_tag_name("tr")
print(len(liste2))
print(liste2)
data = pandas.read_excel("ilk.xlsx")
kelime = data[0]
anlam = data[1]
ana_list = []
ana_list2 = ana_list
liste = list(zip(kelime,anlam))
for i in liste:
    i = list(i)
    ana_list.append(i)
for i in liste2:
    a = i.find_elements_by_tag_name("td")
    # print(f'kelime:{a[0].text} anlamı:{a[1].text}')
    son = [a[0].text,a[1].text]
    if son in ana_list:
        pass
    else:
        anal.append(son)
        ana_list2.append(son)
# print(anal)
print(len(anal))
data1 = pandas.DataFrame(anal)
data1.to_excel("s.xlsx")
data22 = pandas.DataFrame(ana_list2)
data22.to_excel("ilk.xlsx")

driver.close()
