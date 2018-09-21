# -*- coding: utf-8 -*-
"""
plot_zipf_curve.py

형태소 빈도 파일을 읽어서 빈도수 분포의 개형을 보이는 지프 곡선을 그린다.
"""

import sys
import matplotlib.pyplot as plt
from collections import Counter

WORK_PATH="/Users/int_sub05/Desktop/Nohhj/tmc10/text-mining-camp"
MODULE_PATH=WORK_PATH+"/code/common"
sys.path.append(MODULE_PATH)
import ioutil

DATA_PATH=WORK_PATH+"/data"

def plot_zip_curve(morph_counts):
    """
    빈도수 분포의 지프 곡선을 그린다.
    """
    
    count_vals=list(morph_counts.values())
    count_vals=sorted(count_vals, reverse=True)
    plt.plot(count_vals, color="blue", marker="o")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("log(Rank)")
    plt.ylabel("log(Frequency)")
    plt.show()
    
def main(input_file_name):
    """
    형태소 빈도 파일을 읽어서 빈도수 분포의 개형을 보이는 지프 곡선을 그린다.
    """
   
    morph_counts=ioutil.read_morph_counts(input_file_name)
###################################error#######################################
    plot_zip_curve(morph_counts) 
###############################################################################
#
# main
#
    
input_file_name="/Users/int_sub05/.spyder-py3/prac_counter/ai_bib_info.ma.txt"
#input_file_name=sys.argv[1]
main(input_file_name)

