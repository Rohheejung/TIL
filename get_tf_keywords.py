# -*- coding: utf-8 -*-
"""
get_tf_keywords.py

문헌별 키워드를 용어 빈도(TF)에 기반하여 추출한다.
"""

import sys
import ujson
import math
from collections import Counter

WORK_PATH = "C:/Users/int_sub05/Desktop/Nohhj/tmc10/text-mining-camp"
DATA_PATH = WORK_PATH + "/data"

def get_morph_counters(input_file):
    """
    형태소 분석 문헌들을 읽어서 형태소 빈도 계수 객체들을 돌려준다.
    """
    
    mh_morph_counter = Counter()
    mb_morph_counter = Counter()
    
    for line in input_file:
        json_doc = ujson.loads(line.strip())
        
        if json_doc["president"] not in {"노무현", "이명박"}:
            continue
        
        for sent_ma_res in json_doc["body_ma"]:
            for morph_lex, morph_pos in sent_ma_res:
                if morph_pos not in {"NNG", "NNP", "XR", "VV", "VA", "MAG"}:
                    continue
                
                if json_doc["president"] == "노무현":
                    mh_morph_counter[morph_lex] += 1
                else:
                    mb_morph_counter[morph_lex] += 1
                    
    return mh_morph_counter, mb_morph_counter

def get_morph_probs(morph_counter):
    """
    형태소들의 발현 확률을 구하여 돌려준다.
    """
    
    morph_probs = Counter()
    sum_morph_freqs = sum(morph_counter.values())
    
    for morph, freq in morph_counter.items():
        morph_probs[morph] = freq / sum_morph_freqs
        
    return morph_probs

def get_kl_divs(morph_probs_a, morph_probs_b):
    """
    문헌 집합별로 형태소들의 KL 발산을 구하여 돌려준다.
    """
    
    kl_divs_a = Counter()
    kl_divs_b = Counter()
    all_morphs = set(morph_probs_a.keys()) | set(morph_probs_b.keys())
    
    for morph in all_morphs:
        morph_prob_a = morph_probs_a[morph]
        morph_prob_b = morph_probs_b[morph]
        avg_morph_prob = (morph_prob_a + morph_prob_b) / 2
        
        # 형태소 발현 확률이 0이면 KL 발산을 음의 무한대로 정의한다.
        
        if morph_prob_a == 0.0:
            kl_divs_a[morph] = -math.inf
        else:
            kl_divs_a[morph] = morph_prob_a * math.log(morph_prob_a / avg_morph_prob)
            
        if morph_prob_b == 0.0:
            kl_divs_b[morph] = -math.inf
        else:
            kl_divs_b[morph] = morph_prob_b * math.log(morph_prob_b / avg_morph_prob)
    
    return kl_divs_a, kl_divs_b

def write_kl_divs(output_file, kl_divs_a, kl_divs_b):
    """
    문헌 집합별 KL 발산 계산 결과를 출력 파일에 기록한다.
    """
    
    print("MH 연설문 차별어\t\tMB 연설문 차별어", file=output_file)
    
    for (morph_a, kl_div_a), (morph_b, kl_div_b) in zip(kl_divs_a.most_common(50), kl_divs_b.most_common(50)):
        print("{}\t{}\t{}\t{}".format(morph_a, kl_div_a, morph_b, kl_div_b),
              file=output_file)
        
def main(input_file_name, output_file_name):
    """
    문헌 집합별 차별어를 추출하여 기록한다.
    """
    
    with open(output_file_name, "w", encoding="utf-8") as output_file, open(input_file_name, "r", encoding="utf-8") as input_file:
        mh_morph_counter, mb_morph_counter = get_morph_counters(input_file)
        mh_morph_probs = get_morph_probs(mh_morph_counter)
        mb_morph_probs = get_morph_probs(mb_morph_counter)
        mh_kl_divs, mb_kl_divs = get_kl_divs(mh_morph_probs, mb_morph_probs)
        write_kl_divs(output_file, mh_kl_divs, mb_kl_divs)
        
#
# main
#
        
input_file_name = DATA_PATH + "/speeches/speeches.ma.txt"
# input_file_name = sys.argv[1]
output_file_name = DATA_PATH + "/speeches/speeches.kl.txt"
# output_file_name = sys.argv[2]
main(input_file_name, output_file_name)