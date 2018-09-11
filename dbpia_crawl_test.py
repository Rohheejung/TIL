# -*- coding: utf-8 -*-
"""

dbpia_crawl_test.py
"""

# %% 모듈 임포트
import requests
from bs4 import BeautifulSoup

# %% User-Agent 설정
# Requests 모듈의 get() 메소드를 사용할 때에 웹 클라이언트의 User-Agent를 실제 웹 브라우저의
# 것으로 설정하는 것이 안전
# User-Agent는 다음과 같이 딕셔너리로 만들고 나중에 get() 메소드에서 사용한다.
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4)"+\
         "AppleWebKit/537.36 (KHTML, like Gecko)"+\
         "Chrome/37.0.2062.94 Safari/537.36"}

# %% 학술지 페이지 접속과 BeautifulSoup 객체 생성
journal_url="http://www.dbpia.co.kr/Journal/IssueList/PLCT00001088"
response=requests.get(journal_url, headers=headers)
html=response.text
soup=BeautifulSoup(html, "lxml")
print(html)

# %% 권호 페이지 URL 추출
issue_urls=[]
far_outer_elem=soup.select_one("div.sub-menu.a-none")
outer_elems=far_outer_elem.select("dt")

for outer_elem in outer_elems:
    issue_url_elem=outer_elem.select_one("a")
    issue_url=issue_url_elem["href"]
    issue_urls.append(issue_url)
    
print("\n".join(issue_urls))

# %% 권호 페이지 접속과 BeautifulSoup 객체 생성
issue_url="http://www.dbpia.co.kr"+issue_urls[0]
response=requests.get(issue_url, headers=headers)
html=response.text
soup=BeautifulSoup(html, "lxml")
print(html)

# %% 논문 페이지 URL 추출
article_urls=[]
outer_elems=soup.select("div.titleWarp")

for outer_elem in outer_elems:
    article_url_elem=outer_elem.select_one("a")
    article_url=article_url_elem["href"]
    article_urls.append(article_url)
    
print("\n".join(article_urls))

# %% 논문 페이지 접속과 BeautifulSoup 객체 생성
article_url="http://www.dbpia.co.kr/Journal/ArticleDetail/NODE06687470"
response=requests.get(article_url, headers=headers)
html=response.text
soup=BeautifulSoup(html,"lxml")
print(html)

# %% 제목 추출
outer_elem=soup.select_one("div.book_info")
title_elem=outer_elem.select_one("h3")
title=title_elem.string
print(title)

# =============================================================================
# # %% 저자 추출
# author_elem_a_list=[]
# outer_elem=soup.select_one("div.writeInfo")
# author_elems=outer_elem.select_one("span")
# author_elems_a=author_elems.select("a")
# 
# for i in range(0,len(author_elems_a)):
#     author_elem_a_list[i]=author_elems_a[i]
#     print(author_elems_a[i])
#     
# print(author_elem_a_list)
# =============================================================================

# =============================================================================
# # %% 발행연월 추출
# prev_elem=soup.find("dt",string="발행연월")
# print(prev_elem)
# year_mon_elem=prev_elem.find_next()
# year_mon=year_mon_elem.string
# print(year_mon)
# =============================================================================

# %% 초록 추출
abstract_elem=soup.select_one("div.con_txt")
abstract=abstract_elem.text
print(abstract)

bib_info={
        "title":title,
        "author":author,
        "year_mon":year_mon,
        "abstract":abstract
        }
print(bib_info)

#%% 서지 정보 출력
import ujson
bib_info_json=ujson.dumps(bib_info, ensure_ascii=False)
print(bib_info_json)
