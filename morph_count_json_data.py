# -*- coding: utf-8 -*-
"""
morph_count_json_data.py

JSON 라인 형식의 텍스트 집합 형태소 분석 결과에 대상으로 형태소 빈도를
계수하여 출력한다.
"""

import sys
from collections import Counter
import ujson

WORK_PATH="/Users/int_sub05/Desktop/Nohhj/tmc10/text-mining-camp"
DATA_PATH=WORK_PATH+"/data"

def morph_count(input_file, ma_res_keys):
    """
    JSON 라인 형식의 텍스트 집합 형태소 분석 결과에 대상으로 형태소 빈도를
    계수하려 돌려준다.
    """
    
    counter=Counter()
    
    for line in input_file:
        doc=ujson.loads(line.strip())
        for ma_res_key in ma_res_keys:
            if ma_res_key not in doc:
                continue
            for sent_ma_res in doc[ma_res_key]:
                for elem in sent_ma_res:
                    counter[tuple(elem)]+=1
                    
    return counter

def write_counts(output_file, counter):
    """
    빈도 계수 결과를 출력 파일에 기록한다.
    """
    
    for elem, count in counter.most_common():
        morph_lex=elem[0]
        morph_pos=elem[1]
        print("{}\t{}\t{}".format(morph_lex, morph_pos, count), file=output_file)
        
def main(input_file_name, output_file_name, ma_res_keys):
    """
    JSON 라인 형식의 텍스트 집합 형태소 분석 결과에 대상으로 형태소 빈도를
    계수하여 출력한다.
    """
    
    with open(output_file_name, "w", encoding="utf-8") as output_file, open(input_file_name, "r", encoding="utf-8") as input_file:
        counter=morph_count(input_file, ma_res_keys)
        write_counts(output_file, counter)
        
#
# main
#
        
input_file_name="/Users/int_sub05/.spyder-py3/prac_counter/ai_bib_info.ma.txt"
#input_file_name=sys.argv[1]
output_file_name="/Users/int_sub05/.spyder-py3/prac_counter/ai_bib_info.mc.txt"
#output_file_name=sys.argv[2]
ma_res_keys=["title_ma", "abastract_ma"]
# ma_res_keys = sys.argv[3:]
main(input_file_name, output_file_name, ma_res_keys)
