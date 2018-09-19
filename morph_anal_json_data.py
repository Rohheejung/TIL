# -*- coding: utf-8 -*-
"""
morph_anal_json_data.py

JSON 라인 형식의 데이터 파일을 형태소 분석한다.
"""

import sys
import os
import ujson
from konlpy.tag import Komoran
# sys.paht.append("C:\Users\int_sub05\Desktop\노희정\tmc10\text-mining-camp\code\common")
script_dir=os.path.dirname(sys.argv[0])
abs_script_dir=os.path.abspath(script_dir)
module_dir=abs_script_dir+"/../common"
sys.path.append(module_dir)
import textutil

def main(input_file_name,output_file_name,json_keys):
    """
    JSON 라인 형식의 데이터 파일을 형태소 분석한다.
    """
    
    komoran=Komoran()
    
    with open(output_file_name,"w",encoding="utf-8") as output_file, open(input_file_name, "r", encoding="utf-8") as input_file:
        for line in input_file:
            doc=ujson.loads(line.strip())
            for json_key in json_keys:
                if json_key not in doc or not doc[json_key].strip():
                    continue
                ma_res=textutil.get_morph_anal(komoran,doc[json_key])
                doc[json_key+"_ma"]=ma_res
            print(ujson.dumps(doc,ensure_ascii=False),file=output_file)

input_file_name="ai_bib_info.txt"
# input_file_name=sys.argv[1]
output_file_name="ai_bib_info.ma.txt"
# output_file_name = sys.argv[2]
json_keys=["title","abstract"]
# json_keys=sys.argv[3:]
main(input_file_name,output_file_name,json_keys)

