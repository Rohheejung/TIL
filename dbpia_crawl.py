# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:46:11 2018

@author: int_sub05
"""

# 모듈 임포트
import requests
from bs4 import BeautifulSoup
import ujson
import time

# User-Agent 지정
HEADERS = {"User-Agent”: ”Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) " + \
           "AppleWebKit/537.36 (KHTML, like Gecko) " + \
           "Chrome/37.0.2062.94 Safari/537.36"}

# 지연 시간 설정
PAUSE=3

journal_id="PLCT00001088"
output_file_name="disc_cog.txt"

def get_page_soup(url):
    """
    주어진 URL로 접속하여 HTML 얻어 BeautifulSoup 객체를 생성하여 돌려준다.
    """
    
    response=requests.get(url, headers=HEADERS)
    html=response.text
    soup=BeautifulSoup(html, "lxml")
    time.sleep(PAUSE)
    
    return soup

def extract_issue_urls(soup):
    """
    학술지 페이지 객체에서 권호 페이지 url들을 추출하여 돌려준다.
    """
    
    issue_urls=[]
    far_outer_elem=soup.select_one("div.sub-menu.a-none")
    outer_elems=far_outer_elem.select("dt")
    
    for outer_elem in outer_elems:
        issue_url_elem=outer_elem.select_one("a")
        issue_url="http://www.dbpia.co.kr/"+issue_url_elem["href"]
        issue_urls.append(issue_url)
        
    return issue_urls

def extract_article_urls(soup):
    """
    권호 페이지 객체에서 논문 페이지 URL들을 추출하여 돌려준다.
    """
    
    article_urls=[]
    outer_elems=soup.select("div.titleWarp")
    
    for outer_elem in outer_elems:
        article_url_elem=outer_elem.select_one("a")
        article_url="http://www.dbpia.co.kr/"+article_url_elem["href"]
        article_urls.append(article_url)
        
    return article_urls

def extract_title(soup):
    """
    논문 페이지 객체에서 제목을 추출하여 돌려준다.
    """
    
    outer_elem=soup.select_one("div.book_info")
    title_elem=outer_elem.select_one("h3")
    title=title_elem.string
    
    return title

def extract_year_mon(soup):
    """
    논문 페이지 객체에서 발행연월을 추출하여 돌려준다.
    """
    
    prev_elem=soup.find("dt", string="발행연월")
    year_mon_elem=prev_elem.find_next()
    year_mon=year_mon_elem.string
    
    return year_mon

def extract_abstract(soup):
    """
    논문 페이지 객체에서 초록을 추출하여 돌려준다.
    """
    abstract_elem=soup.select_one("div.con_txt")
    abstract=abstract_elem.text.strip()
    
    return abstract

def build_bib_info(title, author, year_mon, abstract):
    """
    주어진 서지 정보 항목들을 조합하여 딕셔너리 객체를 만들어 돌려준다.
    """
    
    bib_info={
            "title":title,
            "author":author,
            "year_mon":year_mon,
            "abstract":abstract
            }
    
    return bib_info

def write_bib_info(output_file, bib_info):
    """
    구조화된 서지 정보를 출력 파일에 기록한다.
    """
    
    bib_info_json=ujson.dumps(bib_info, ensure_ascii=False)
    print(bib_info_json, file=output_file)
    
def main(journal_id, output_file_name):
    """
    주어진 학술지 식별자로 확인되는 학술지의 모든 권호에 실린 모든 논문의
    서지 정보를 수집하여 출력 파일에 기록한다.
    """
    
    with open(output_file_name, "w", encoding="utf-8") as output_file:
        journal_url="http://www.dbpia.co.kr/Journal/IssueList/"+journal_id
        journal_soup=get_page_soup(journal_url)
        issue_urls=extract_issue_urls(journal_soup)
        
        for issue_url in issue_urls:
            issue_soup=get_page_soup(issue_url)
            article_urls=extract_article_urls(issue_soup)
            
            for article_url in article_urls:
                article_soup=get_page_soup(article_url)
                title=extract_title(article_soup)
                author=extract_author(article_soup)
                year_mon=extract_year_mon(article_soup)
                abstract=extract_abstract(article_soup)
                bib_info=build_bib_info(title, author, year_mon, abstract)
                write_bib_info(output_file, bib_info)
                
main(journal_id, output_file_name)