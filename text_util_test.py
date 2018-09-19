# -*- coding: utf-8 -*-
"""
text_util_test.py

textutil.py의 기능을 실험한다.
"""

# %% 사용자 모듈 임포트
import os
import sys
from konlpy.tag import Komoran

# sys.path는 파이썬 인터프리터에서 라이브러리 모듈을 탐색하는 디렉토리들이
# 담겨 있는 리스트이다. 이 리스트에 사용자 모듈이 포함된 디렉토리를 추가하면
# 임포트하여 사용할 수 있다. 이 강좌에서의 약속은 모듈을 주차별 예제 코드가
# 들어 있는 01,02,03 등의 디렉토리와 같은 수준에 common이라는 디렉토리를
# 만들어 저장하는 것이다. 그런데 문제는 이 디렉토리의 위치는 사용자 환경에
# 그 절대 위치가 달라질 수 있다는 것이다. 그러므로 실행 스크립트의 경로로부터
# 모듈 디렉토리의 절대 경로를 알아내야 한다.
# 그러나 실제 상황에서는 사용자 모듈을 저장하는 위치가 고정되어 있으므로
# 다음 예와 같이 직접 지정하는 것이 훨씬 편리할 것이다.
# sys.path.append("C:\Users\int_sub05\Desktop\노희정\tmc10\text-mining-camp\code\common")
script_dir=os.path.dirname(sys.argv[0])
abs_script_dir=os.path.abspath(script_dir)
module_dir=abs_script_dir+"/../common"
sys.path.append(module_dir)
import textutil
print(dir(textutil))

# %% 입력 텍스트 선언
my_text="""<벌레이야기>

1
아내는 알암이의 돌연스런 가출이 유괴에 의한 실종으로 확실시되고 난 다음에도 한동안은 악착스럽게 자신을 잘 견뎌 나가고 있었다. 그것은 아이가 어쩌면 행여 무사히 되돌아오게 될지도 모른다는 간절한 희망과, 녀석에게 마지막 불행한 일이 생기기 전에 어떻게든지 놈을 다시 찾아내고 말겠다는 어미로서의 강인한 의지와 기원 때문인 것 같았다.
지난해 5월 초. 어느 날 알암이가 학교에서 돌아올 시각이 훨씬 지나도록 귀가를 안 했다.
"""

# %% 형태소 분석기 객체 초기화
komoran=Komoran()

# %% 리스트 객체로 형태소 분석 결과 받기
ma_res=textutil.get_morph_anal(komoran,my_text)
for sent_num,sent_anal in enumerate(ma_res,1):
    print("문장 {} 형태소 분석 결과".format(sent_num))
    for lex,pos in sent_anal:
        print("{}\t{}".format(lex,pos))
    print()
print()

# %% JSON 문자열로 형태소 분석 결과 받기
ma_res_json=textutil.get_morph_anal_json(komoran,my_text)
print(ma_res_json)
print()

# %% 수직 문자열로 형태소 분석 결과 받기
ma_res_vert=textutil.get_morph_anal_vert(komoran,my_text)
print(ma_res_vert)
print()

# %% 수평 문자열로 형태소 분석 결과 받기
ma_res_hori=textutil.get_morph_anal_hori(komoran,my_text)
print(ma_res_hori)
print()

