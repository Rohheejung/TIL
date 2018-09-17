# -*- coding: utf-8 -*-
"""
morph_anal_test.py

형태소 분석기를 실험한다.
"""

from konlpy.tag import Komoran

komoran=Komoran()

while True:
    text=input("분석할 텍스트를 입력하세요: ")
    
    if not text.strip():
        break
    
    ma_result=komoran.pos(text)
    
    for lex, pos in ma_result:
        print("{}\t{}".format(lex,pos))
        
    print()

