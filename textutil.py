# -*- coding: utf-8 -*-
"""
textutil.py

텍스트 유틸리티 함수 모음
"""

import ujson

def split_sentences(text):
    """
    입력 문자열을 문장들의 리스트로 만들어 돌려준다.
    """
    
    new_text=text.replace(". ",".\n").replace("? ","?\n").replace("! ","!\n")
    
    sentences=[]
    for sentence in new_text.splitlines():
        if not sentence.strip():
            continue
        
        sentences.append(sentence)
        
    # 리스트 내포를 사용하면 아래와 같이 할 수 있다.
    # sentences = [s for s in new_text.splitlines() if s.strip()]
    
    return sentences

def get_morph_anal(analyzer,text,split_sentence=True,keep_wordform=False):
    """
    주어진 텍스트에 대해 형태소 분석을 수행하여 결과를 돌려준다.
    """
    
    if split_sentence:
        morph_anal=[]
        for sent in split_sentence(text):
            sent_morph_anal=analyzer.pos(sent,flatten=not keep_wordform)
            morph_anal.append(sent_morph_anal)
    else:
        morph_anal=analyzer.pos(text,flatten=not keep_wordform)
        
    return morph_anal

def get_morph_anal_json(analyzer,text,split_sentence=True,keep_wordform=False):
    """
    주어진 텍스트에 대해 형태소 분석을 수행하여 결과를 돌려준다.
    """
    
    morph_anal=get_morph_anal(analyzer,text,split_sentence,keep_wordform)
    json_obj={
            "text":text,
            "morphAnal":morph_anal
            }
    morph_anal_json=ujson.dumps(json_obj,ensure_ascii=False)
    
    return morph_anal_json

def get_morph_anal_vert(analyzer,text):
    """
    주어진 텍스트에 대해 형태소 분석을 수행하여 결과를 돌려준다.
    """
    
    text_morph_anal_vert_elems=[]
    sents=split_sentences(text)
    
    for sent in sents:
        vert_elems=[]
        wordforms=sent.split()
        morph_anal=get_morph_anal(analyzer,sent,split_sentence=False,keep_wordform=True)
        
        for wordform,wordform_anal in zip(wordforms,morph_anal):
            morphs=[]
            
            for lex,pos in wordform_anal:
                morphs.append(lex+"/"+pos)
                
            vert_elems.append(wordform+"\t"+"+".join(morphs))
            
        morph_anal_vert="\n".join(vert_elems)
        text_morph_anal_vert_elems.append(morph_anal_vert)
        
    text_morph_anal_vert="\n\n".join(text_morph_anal_vert_elems)
    
    return text_morph_anal_vert

def get_morph_anal_hori(analyzer,text):
    """
    주어진 텍스트에 대해 형태소 분석을 수행하여 결과를 돌려준다.
    """
    
    text_morph_anal_hori_elems=[]
    sents=split_sentences(text)
    
    for sent in sents:
        hori_elems=[]
        wordforms=sent.split()
        morph_anal=get_morph_anal(analyzer,sent,split_sentence=False,keep_wordform=True)
        
        for wordform,wordform_anal in zip(wordforms,morph_anal):
            morphs=[]
            
            for lex,pos in wordform_anal:
                morphs.append(lex+"/"+pos)
                
            hori_elems.append(wordform+"_"+"+".join(morphs))
            
        morph_anal_hori=" ".join(hori_elems)
        text_morph_anal_hori_elems.append(morph_anal_hori)
        
    text_morph_anal_hori="\n".join(text_morph_anal_hori_elems)
    
    return text_morph_anal_hori
