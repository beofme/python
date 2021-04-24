
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://www.naver.com'
page = urlopen(url)
soup = BeautifulSoup(page,'lxml')
print(soup)


import time

S = time.time()

BeautifulSoup(page, 'lxml')

lxml_time = time.time() - S

S = time.time()

BeautifulSoup(page,'html.parser')

html_parser_time = time.time() - S

S = time.time()

BeautifulSoup(page,'html5lib')

html5lib_time = time.time() - S


print(f'lxml 시간 측정 : {lxml_time}초')

print(f'html.parser 시간 측정 : {html_parser_time}초')

print(f'html5lib 시간 측정 : {html5lib_time}초')
