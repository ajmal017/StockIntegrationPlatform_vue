# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:28:59 2020

@author: User
"""
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import json


path = "D:\selenium_driver_chrome\chromedriver.exe" #chromedriver.exe執行檔所存在的路徑

driver = webdriver.Chrome(path)
#driver = webdriver.Chrome()
driver.get('https://mops.twse.com.tw/mops/web/t05st03')

#輸入股票代碼
#變數名稱
# stockid="2330"
stockid=sys.argv[1]
driver.find_element_by_id('co_id').send_keys(stockid)#找id=email
driver.find_element_by_id('co_id').send_keys(Keys.ENTER)
time.sleep(1) #這很重要
###############################################開始抓基本資料

#soup = BeautifulSoup(browser.page_source, 'html.parser')
#soup = BeautifulSoup(driver.page_source, 'html.parser')

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()


table=soup.find('table', class_ = 'hasBorder')
#table.contents


#table = soup.find_all('table', class='hasBorder')
#table=table1[1]


table_all=table.find_all('td')


basic_data=[]

for i in range(0,len(table_all)):
    basic_data.append(table_all[i].text)


##########################輸出成dict
basic_dict = {
              #公司名稱
             "company": basic_data[3],
              #產業類別
             "industry": basic_data[1].strip().replace(u'\u3000', u' ').replace(u'\xa0', u' '),
             #成立時間
             "start_time": basic_data[13],
             #上市(櫃)時間
             "IPO":basic_data[16],
             #董事長
             "Chairman":basic_data[6],

             #實收資本額
             "capital":basic_data[15].strip(),

             #已發行普通股數
             "publiccommon_stock":basic_data[21].replace(" ", "").replace('\n',''),


             #普通股每股面額
             "common_stock":basic_data[20].replace(" ", ""),


              #特別股每股面額
             "preferred_stock":basic_data[22].replace(" ", ""),

             #投資人關係聯絡人
             "investman":basic_data[41],

             #主要經營業務
            "Main_business":basic_data[12],

                }



#finalbasic= json.dumps(basic_dict,ensure_ascii=False)
finalbasic= json.dumps(basic_dict)
print(finalbasic)

