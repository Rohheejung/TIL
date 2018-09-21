# -*- coding: utf-8 -*-
"""
draw_word_cloud.py

형태소 빈도 파일을 읽어서 워드 클라우드를 그린다.
"""

import sys
import matplotlib.pyplot as plt
import wordcloud

WORK_PATH="/Users/int_sub05/Desktop/Nohhj/tmc10/text-mining-camp"
MODULE_PATH=WORK_PATH+"/code/common"
sys.path.append(MODULE_PATH)
import ioutil

DATA_PATH=WORK_PATH+"/data"
BACKGROUND_COLOR="black"
WIDTH=1500
HEIGHT=900
#윈도우 사용자는 아래와 같은 글꼴을 지정한다.
FONT_PATH="C:/Windows/Fonts/malgun.ttf"

def generate_text(morph_counts):
    """
    워드 클라우드의 입력으로 쓸 텍스트를 생성하여 돌려준다.
    """
    
    text_morphs=[]
    
    for morph, count in morph_counts.most_common():
        # 어휘 빈도를 작은 수로 조정한다.
        count=int(round(count/10))
        morph_lex=morph[0]
        sub_text_morphs=[morph_lex]*count
        text_morphs.extend(sub_text_morphs)
        # 위는 아래와 같은 표현이다
        # text_morphs+=sub_text_morphs
        
    text=" ".join(text_morphs)
    
    return text

def draw_cloud(text):
    """
    워드 클라우드를 생성하여 돌려준다.
    """
    
    cloud_gen=wordcloud.WordCloud(background_color=BACKGROUND_COLOR,
                                  width=WIDTH, height=HEIGHT,
                                  font_path=FONT_PATH)
    cloud=cloud_gen.generate(text)
    
    return cloud

def show_cloud(cloud):
    """
    워드 클라우드를 화면에 표시한다.
    """
    
    plt.imshow(cloud)
    plt.axis("off")
    plt.show()
    
def main(input_file_name):
    """
    형태소 빈도 파일을 읽어서 워드 클라우드를 그린다.
    """
    
    morph_counts=ioutil.read_morph_counts(input_file_name, top_n=200,
                                          in_poses={"NNG"})
    text=generate_text(morph_counts)
    cloud=draw_cloud(text)
    show_cloud(cloud)
    
#
# main
#
input_file_name="/Users/int_sub05/.spyder-py3/prac_counter/ai_bib_info.mc.txt"
#input_file_name=sys.argv[1]
main(input_file_name)
