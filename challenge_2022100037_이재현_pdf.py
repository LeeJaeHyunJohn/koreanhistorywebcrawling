# -*- coding: utf-8 -*-
"""CHALLENGE_2022100037_이재현.pdf

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pbvk_YNpp0W3E8GoknGe7-wnUXa0KtTL
"""

#셀레늄 사용을 위한 설치

import sys

!sudo add-apt-repository ppa:saiarcot895/chromium-beta
!sudo apt remove chromium-browser
!sudo snap remove chromium
!sudo apt install chromium-browser

!pip install selenium
!apt-get update
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

input_data = list(map(str, input().split()))
input_data[0] = input_data[0] + '회차'
my_answer = []
my_score = 0
for _ in range(5):
    buffer = list(map(str, input().split()))
    for i in buffer:
        i = list(i)
        for temp in i:
            my_answer.append(temp)


specific_options = webdriver.ChromeOptions()
specific_options.add_argument('--headless')
specific_options.add_argument('--no-sandbox')
specific_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options = specific_options)
driver.get('https://www.historyexam.go.kr/answer/list.do?netfunnel_key=0581D74DF20AE8FF35B5550992752077D3831348D8723D03CB13C9E714A1859E939F36D134FF486DA323538AE2723C55C77335B843295DFC253D04AA3C9A4E91EE0F79750ABA2F48FE0F857A0E9F921350065359E3BB58BA1683B652D53F0FEF4A0C0A3BF7217CB6E84A246F8DC2BD142C30')
#driver.get('http://www.historyexam.go.kr/answer/list.do')
time.sleep(1)

times_box = driver.find_element(By.NAME, 'times')
times_box.send_keys(input_data[0])
testlevel_box = driver.find_element(By.NAME, 'testlevel')
testlevel_box.send_keys(input_data[1])

button_xpath = '//*[@id="sub_content"]/div[2]/div[3]/form/div/div[3]/a/img'
button = driver.find_element(By.XPATH, button_xpath)
button.click()
time.sleep(1)

soup = BeautifulSoup(driver.page_source, 'html.parser')
Data = soup.find_all('td')
ans_1 = []
ans_2 = []
scr_1 = []
scr_2 = []
flag = 0
for index in Data:
    index = index.text
    index = index.strip()
    if flag % 4 == 0:
        ans_1.append(index)
    elif flag % 4 == 1:
        scr_1.append(index)
    elif flag % 4 == 2:
        ans_2.append(index)
    else:
        scr_2.append(index)
    flag += 1

for i in range(50):
    if i < 25:
        if my_answer[i] == ans_1[i] or ans_1[i] == '없음':
            my_score += int(scr_1[i])
    else:
        if my_answer[i] == ans_2[i - 25] or ans_2[i - 25] == '없음':
            my_score += int(scr_2[i - 25])
print(my_score)