# -*- coding: utf-8 -*-
"""
counter_test.py

계수에 특화된 자료 구조를 제공하는 Counter 클래스를 실험한다.
"""

# %% 모듈 임포트
import sys
# Counter 클래스를 이용하려면 clooections 모듈을 임포트해야 한다.
from collections import Counter
from konlpy.tag import Komoran

# %% 사용자 모듈 임포트
# WORK_PATH 변수에 사용자의 text-mining-camp 디렉토리 경로를 지정한다.
WORK_PATH="/Users/int_sub05/Desktop/Nohhj/tmc10/text-mining-camp"
MODULE_PATH=WORK_PATH+"/code/common"
sys.path.append(MODULE_PATH)
import textutil

# %% 입력 문자열 정의
my_text="""<벌레이야기>

1
아내는 알암이의 돌연스런 가출이 유괴에 의한 실종으로 확실시되고 난 다음에도 한동안은 악착스럽게 자신을 잘 견뎌 나가고 있었다. 그것은 아이가 어쩌면 행여 무사히 되돌아오게 될지도 모른다는 간절한 희망과, 녀석에게 마지막 불행한 일이 생기기 전에 어떻게든지 놈을 다시 찾아내고 말겠다는 어미로서의 강인한 의지와 기원 때문인 것 같았다.
지난해 5월 초. 어느 날 알암이가 학교에서 돌아올 시각이 훨씬 지나도록 귀가를 안 했다.
"""

# %% 형태소 분석기 객체 초기화
komoran=Komoran()

# %% Counter 객체 초기화
counter=Counter()

# %% 형태소 분석 실행
ma_res=textutil.get_morph_anal(komoran, my_text)

# %% 형태소 빈도 계수 (직접 계수)
for sent_ma_res in ma_res:
    for morph_lex, morph_pos in sent_ma_res:
        counter[(morph_lex, morph_pos)]+=1
        
# %% 형태소 빈도 계수 결과 출력 (빈도 역순)
print("빈도 역순 출력")
for(morph_lex, morph_pos), freq in counter.most_common():
    print("{}\t{}\t{}".format(morph_lex, morph_pos, freq))
    
# %% Counter 객체 초기화
counter=Counter()

# %% 형태소 빈도 계수 (간접 계수)
for sent_ma_res in ma_res:
    counter.update(sent_ma_res)
    
# %% 형태소 빈도 계수 결과 출력 (형태소 사전순)
print("형태소 사전순 출력")
for morph in sorted(counter.elements()):
    morph_lex=morph[0]
    morph_pos=morph[1]
    count=counter[morph]
    print("{}\t{}\t{}".format(morph_lex, morph_pos, freq))