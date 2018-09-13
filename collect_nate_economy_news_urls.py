# -*- coding: utf-8 -*-
"""
collect_nate_economy_news_urls.py

네이트 경제 뉴스 기사 URL을 수집한다.
"""

import sys
import time
import re
import requests

def create_output_file(target_data):
    """
    출력 파일을 생성하고 파일 객체를 돌려준다.
    """
    
    output_file_name="article_urls."+target_data+".txt"
    output_file=open(output_file_name,"w",encoding="utf-8")
    
    return output_file

def get_html(target_data,page_num):
    """
    주어진 날짜와 페이지 번호에 해당하는 페이지 URL에 접근하여 HTML을
    돌려준다.
    """
    
    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) " + \
        "AppleWebKit/537.36 (KHTML, like Gecko) " + \
        "Chrome/37.0.2062.94 Safari/537.36"
    headers = {"User-Agent": user_agent}

    page_url = "http://news.nate.com/recent?cate=eco&mid=n0301&type=t&"+\
        "date="+target_data+"&page="+str(page_num)
        
    response=requests.get(page_url,headers=headers)
    html=response.text
    
    return html

def paging_done(html):
    """
    페이징이 완료되었는지를 판단한다.
    """
    
    done_pat=u"뉴스가 없습니다."
    
    if done_pat in html:
        return True
    
    return False

def ext_news_article_urls(html):
    """
    주어진 HTML에서 기사 URL을 추출하여 돌려준다.
    """
    
    url_frags=re.findall('<a href="(.*?)"',html)
    news_article_urls=[]
    
    for url_frag in url_frags:
        if not url_frag.startswith("/view/"):
            continue
        
        url="http://news.nate.com"+url_frag
        news_article_urls.append(url)
        
    return news_article_urls

def write_news_article_urls(output_file,urls):
    """
    기사 URL들을 출력 파일에 기록한다.
    """
    
    for url in urls:
        # output_file.write("{}\n".format(url))
        print(url, file=output_file)
        
def pause():
    """
    2초 동안 쉰다.
    """
    
    time.sleep(2)
    
def close_output_file(output_file):
    """
    출력 파일을 닫는다.
    """
    
    output_file.close()
    
def main(target_data):
    """
    주어진 수집 대상 날짜의 네이트 경제 뉴스 기사 URL을 수집한다.
    """
    
    output_file=create_output_file(target_data)
    page_num=1
    
    while True:
        html=get_html(target_data,page_num)
        
        if paging_done(html):
            break
        
        urls=ext_news_article_urls(html)
        write_news_article_urls(output_file,urls)
        page_num+=1
        pause()
        
    close_output_file(output_file)
    
#target_data=sys.argv[1]
target_data="20180912"
main(target_data)

