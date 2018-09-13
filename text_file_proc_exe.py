# -*- coding: utf-8 -*-
"""
text_file_proc_exe.py

텍스트 파일 처리 연습
"""

def split_sentences(text):
    """
    입력 문자열을 문장들의 리스트로 만들어 돌려준다.
    
    인자
    ----
    text:string
        입력 문자열
        
    반환값
    ------
    sentences:list
        문장의 리스트. 각 문장은 문자열이다.
        
    참고
    ----
    마침표(.), 물음표(?), 느낌표(!)에 바로 이어서 공백 문자가 있으면 문장을 나눈다.
    빈 문장은 제외한다.
    """
    
    next_text=text.replace(". ",".\n").replace("? ","?\n").replace("! ","\n")
    
    sentences=[]
    
    for sent in next_text.splitlines():
        if not sent:
            continue
        
        sentences.append(sent)
        
    return sentences

def count_sents(text):
    """
    입력 문자열에 포함된 문장 수를 계수하여 돌려준다.
    
    인자
    ----
    text:string
        입력 문자열
        
    반환값
    ------
    sent_count:int
        문장 수
    """
    
    sents=split_sentences(text)
    sent_count=len(sents)
    
    return sent_count

def count_words(text):
    """
    입력 문자열의 어절 수를 계수하여 돌러준다.
    
    인자
    ----
    text:string
        입력 문자열
    
    반환값
    ------
    word_count:int
        어절 수
        
    참고
    ----
    어절의 구분은 공백문자로 한다.
    """
    
    words=text.split()
    word_count=len(words)
    
    return word_count

def count_chars(text):
    """
    입력 문자열의 문자 수를 계수하여 돌려준다.
    
    인자
    ----
    text:string
        입력 문자열
        
    반환값
    ------
    char_count:int
        문자 수
        
    참고
    ----
    공백문자는 계수에서 제외한다.
    """
    
    char_count=0
    
    for char in text:
        if char.isspace():
            continue
        
        char_count+=1
        
    return char_count

def main(input_file_name):
    """
    입력 파일에서 텍스트를 읽어서 라인 수, 문장 수, 어절 수,
    문자 수를 계수하여 출력한다.
    
    인자
    ----
    input_file_name:string
        입력 파일 이름
    """
    
    line_count=0
    sent_count=0
    word_count=0
    char_count=0
    
    with open(input_file_name,"r",encoding="utf-8") as input_file:
        for line in input_file:
            if not line:
                continue
            
            line_count+=1
            sent_count+=count_sents(line)
            word_count+=count_words(line)
            char_count+=count_chars(line)
            
    print("Number of lines: {}".format(line_count))
    print("Number of sentences: {}".format(sent_count))
    print("Number of words: %s" %word_count)
    print("Number of characters: %s" %char_count)
    
input_file_name="C:/Users/int_sub05/.spyder-py3/worm.txt"
main(input_file_name)
