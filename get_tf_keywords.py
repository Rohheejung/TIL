# -*- coding: utf-8 -*-
"""
get_tf_keywords.py

문헌별 키워드를 용어 빈도(TF)에 기반하여 추출한다.
"""

import sys
import ujson
from collections import Counter

WORK_PATH="/Users/int_sub05/Desktop/Nohhj/tmc10/text-mining-camp"
DATA_PATH=WORK_PATH+"/data"

def read_documents(input_file):
    """
    형태소 분석 문헌들을 읽어서 돌려준다.
    """
    
    docs=[]
    
    for line in input_file:
        json_doc=ujson.loads(line.strip())
        
        if "abstract_ma" not in json_doc:
            continue
        
        morphs=[]
        
        for json_key in ["title_ma","abstract_ma"]:
            for sent_ma_res in json_doc[json_key]:
                for morph_lex, morph_pos in sent_ma_res:
                    if morph_pos not in {"NNG","NNP","XR"}:
                        continue
                    
                    morphs.append(morph_lex)
                    
        ma_doc={
                "title":json_doc["title"],
                "abstract":json_doc["abstract"],
                "morphs":morphs
                }
        docs.append(ma_doc)
        
    return docs

def get_term_freq_counters(docs):
    """
    주어진 문헌 집합으로부터 용어 빈도 리스트를 생성하여 돌려준다.
    """
    
    term_freq_counters=[]
    
    for doc in docs:
        term_freq_counter=Counter()
        term_freq_counter.update(doc["morphs"])
        term_freq_counters.append(term_freq_counter)
        
    return term_freq_counters

def extract_tf_keywords(term_freq_counters):
    """
    용어 빈도 기반 문헌별 키워드를 추출하여 돌려준다.
    """
    
    tf_keywords=[]
    
    for term_freq_counter in term_freq_counters:
        keywords=[]
        for term, term_freq in term_freq_counter.most_common(10):
            keywords.append(term)
            tf_keywords.append(keywords)
            
        return tf_keywords

def write_keywords(output_file, docs, tf_keywords):
    """
    문헌별 키워드를 출력 파일에 기록한다.
    """
    
    for doc, keywords in zip(docs, tf_keywords):
        print("제목: {}".format(doc["title"]), file=output_file)
        print("요약문: {}".format(doc["abstract"]), file=output_file)
        print("키워드: {}".format(", ".join(keywords)), file=output_file)
        print("="*60, file=output_file)
        
def main(input_file_name, output_file_name):
    """
    문헌별 키워드를 용어 빈도(TF)에 기반하여 추출한다.
    """
    
    with open(output_file_name, "w", encoding="utf-8") as output_file, open(input_file_name, "r", encoding="utf-8") as input_file:
        docs=read_documents(input_file)
        term_freq_counters=get_term_freq_counters(docs)
        tf_keywords=extract_tf_keywords(term_freq_counters)
        write_keywords(output_file, docs, tf_keywords)
        
#
# main
#
        
input_file_name="/Users/int_sub05/.spyder-py3/prac_counter/ai_bib_info.ma.txt"
#input_file_name=sys.argv[1]
output_file_name="/Users/int_sub05/.spyder-py3/prac_counter/ai_bib_info.tf.txt"
#output_file_name=sys.argv[2]
main(input_file_name, output_file_name)
    


