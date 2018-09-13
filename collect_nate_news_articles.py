# -*- coding: utf-8 -*-
"""
collect_nate_news_articles.py

네이트 뉴스 기사를 수집한다.
"""

import sys
import time
import requests

def open_url_file(target_data):
    """
    URL 파일을 연다.
    """
    
    url_file_name="article_urls.{}.txt".format(target_data)
    url_file=open(url_file_name,"r",encoding="utf-8")
    
    return url_file

def create_html_file(target_data):
    """
    출력 파일을 생성한다.
    """
    
    html_file_name="article_htmls.{}.txt".format(target_data)
    html_file=open(html_file_name,"w",encoding="utf-8")
    
    return html_file

def gen_print_url(url_line):
    """
    주어진 기사 링크 URL로부터 인쇄용 URL을 만들어 돌려준다.
    """
    
    p=url_line.rfind("/")
    q=url_line.rfind("?")
    article_id=url_line[p+1:q]
    print_url="http://news.nate.com/view/print?aid="+article_id
    
    return print_url

def get_html(print_url):
    """
    주어진 인쇄용 URL에 접근하여 HTML을 읽어서 돌려준다.
    """
    
    user_agent="Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 " + \
        "(KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    headers = {
            "User-Agent": user_agent
            }
        
    response=requests.get(print_url,headers=headers)
    html=response.text
    
    return html

def write_html(output_file, html):
    """
    주어진 HTML 텍스트를 출력 파일에 쓴다.
    """
    
    # output_file.write("{}\n".format(html))
    # output_file.write("@@@@@ ARTICLE DELIMITER @@@@@\n")
    print(html, file=output_file)
    print("@@@@@ ARTICLE DELIMITER @@@@@",file=output_file)
    
def pause():
    """
    3초 동안 쉰다.
    """
    
    time.sleep(3)
    
def close_output_file(output_file):
    """
    출력 파일을 닫는다.
    """
    
    output_file.close()

def close_url_file(url_file):
    """
    URL 파일을 닫는다.
    """
    
    url_file.close()
    
def main(target_data):
    """
    주어진 URL 파일로부터 URL을 읽어서 네이트 뉴스 기사를 수집하여
    HTML 출력 파일에 기록한다.
    """
    
    url_file=open_url_file(target_data)
    html_file=create_html_file(target_data)
    
    for line in url_file:
        print_url=gen_print_url(line)
        html=get_html(print_url)
        write_html(html_file,html)
        
    close_output_file(html_file)
    close_url_file(url_file)
    
# target_date=sys.argv[1]
target_date="20180912"
main(target_date)
