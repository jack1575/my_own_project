import requests
from bs4 import BeautifulSoup
from selenium import webdriver

f = open('스파이더맨.txt', 'w', encoding='utf-8')


driver = webdriver.Chrome('C:/Users/jack1/Desktop/import/chromedriver_win32/chromedriver')

for i in range(1, 11):
    for j in range(1, 11):
        driver.get('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=173123&target=after&page=' + str(i))
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        notices1 = soup.select('#old_content > table > tbody > tr:nth-of-type(' + str(j) + ')> td.title')

        for n in notices1:
            a = n.text.strip()
            a = str(a).replace("신고", "")
            a = str(a).replace(",", "")
        f.write(str(a)+',')

f.close()
