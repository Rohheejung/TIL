# -*- coding: utf-8 -*-
"""
post_proc_test.py

형태소 분석 결과를 후처리를 실험한다.
"""

import sys
import os
from konlpy.tag import Komoran
# sys.path.append("C:/Users/int_sub05/Desktop/노희정/tmc10/text-mining-camp/code/common")
script_dir=os.path.dirname(sys.argv[0])
abs_script_dir=os.path.abspath(script_dir)
module_dir=abs_script_dir+"/../common"
sys.path.append(module_dir)
import textutil

# %% 후처리 함수 정의
def post_proc(morph_anal):
    """
    형태소 분석 결과를 후처리하여 돌려준다.
    """
    
    post_morph_anal=post_proc_pre_noun_deriv(morph_anal)
    post_morph_anal=post_proc_post_noun_deriv(post_morph_anal)
    post_morph_anal=post_proc_pred_deriv(post_morph_anal)
    
    return post_morph_anal

_ROOT_POSES=["XR","NNG","MAG"]

def post_proc_pre_noun_deriv(morph_anal):
    """
    명사접두 파생에 대한 후처리를 수행한다.
    """
    
    post_morph_anal=[]
    
    for wordform_anal in morph_anal:
        if len(wordform_anal)<2:
            post_morph_anal.append(wordform_anal)
            continue
        
        if wordform_anal[0][1]=="XPN" and wordform_anal[1][1] in _ROOT_POSES:
            new_pos="NNG"
            new_lex=wordform_anal[0][0]+wordform_anal[1][0]
        else:
            post_morph_anal.append(wordform_anal)
            continue
        
        new_wordform_anal=[(new_lex,new_pos)]+wordform_anal[2:]
        post_morph_anal.append(new_wordform_anal)
        
    return post_morph_anal

def post_proc_post_noun_deriv(morph_anal):
    """
    명사 접미 파생에 대한 후처리를 수행한다.
    """
    
    post_morph_anal=[]
    
    for wordform_anal in morph_anal:
        if len(wordform_anal)<2:
            post_morph_anal.append(wordform_anal)
            continue
        
        if wordform_anal[0][1] in _ROOT_POSES and wordform_anal[1][1]=="XSN":
            new_pos="NNG"
            new_lex=wordform_anal[0][0]+wordform_anal[1][0]
        else:
            post_morph_anal.append(wordform_anal)
            continue
        
        new_wordform_anal=[(new_lex,new_pos)]+wordform_anal[2:]
        post_morph_anal.append(new_wordform_anal)
        
    return post_morph_anal

def post_proc_pred_deriv(morph_anal):
    """
    용언 파생에 대한 후처리를 수행한다.
    """
    
    post_morph_anal=[]
    
    for wordform_anal in morph_anal:
        if len(wordform_anal)<2:
            post_morph_anal.append(wordform_anal)
            continue
        
        if wordform_anal[0][1] in _ROOT_POSES and wordform_anal[1][1]=="XSA":
            new_pos="VA"
        elif wordform_anal[0][1] in _ROOT_POSES and wordform_anal[1][1]=="XSV":
            new_pos="VV"
        else:
            post_morph_anal.append(wordform_anal)
            continue
        
        new_lex=wordform_anal[0][0]+wordform_anal[1][0]
        new_wordform_anal=[(new_lex,new_pos)]+wordform_anal[2:]
        post_morph_anal.append(new_wordform_anal)
        
    return post_morph_anal

# %% main() 함수 정의
def main():
    """
    형태소 분석 결과를 후처리를 실험한다.
    """
    
    komoran=Komoran()
    my_text="""<벌레이야기>

1
아내는 알암이의 돌연스런 가출이 유괴에 의한 실종으로 확실시되고 난 다음에도 한동안은 악착스럽게 자신을 잘 견뎌 나가고 있었다. 그것은 아이가 어쩌면 행여 무사히 되돌아오게 될지도 모른다는 간절한 희망과, 녀석에게 마지막 불행한 일이 생기기 전에 어떻게든지 놈을 다시 찾아내고 말겠다는 어미로서의 강인한 의지와 기원 때문인 것 같았다.
지난해 5월 초. 어느 날 알암이가 학교에서 돌아올 시각이 훨씬 지나도록 귀가를 안 했다.
"""
    
    ma_res=textutil.get_morph_anal(komoran,my_text,split_sentence=True,keep_wordform=True)
    for sent_ma_res in ma_res:
        sent_ma_res=post_proc(sent_ma_res)
        for wordform_anal in sent_ma_res:
            print(wordform_anal)
        print()
        
# %% main() 함수 호출
main()
