# -*- coding: utf-8 -*-

"""
ioutil.py

입출력 유틸리티 함수 모음
"""

from collections import Counter
import ujson


def read_morph_counts(morph_count_file_name, top_n=0, in_poses=set()):
    """
    형태소 빈도 파일에서 상위 빈도 계수 결과를 읽어서 돌려준다.

    인자
    ----
    morph_count_file_name : 문자열
        형태소 빈도 계수 파일 이름

    top_n : 정수 (default: 0)
        읽어들일 상위 빈도 순위 수. 0이면 전체를 읽는다.

    in_poses: 세트 (default: set())
        읽어들일 품사를 지정하는 세트. 공집합이면 전체를 읽는다.

    반환값
    ------
    morph_counts : Counter 객체
        형태소 빈도 계수 결과를 담는다.
    """

    morph_counts = Counter()

    with open(morph_count_file_name, "r", encoding="utf-8") as \
            morph_count_file:
        for line in morph_count_file:
            morph_lex, morph_pos, count = line.strip().split("\t")

            if in_poses and morph_pos not in in_poses:
                continue

            morph_counts[(morph_lex, morph_pos)] = int(count)

            if top_n > 0 and len(morph_counts) > top_n:
                break

    return morph_counts


def read_documents(input_file_name, json_keys, with_pos=False,
                   in_poses=set()):
    """
    JSON 라인 형식의 형태소 분석 파일에서 형태소 분석된 문헌들을
    읽어서 돌려준다.

    인자
    ----
    input_file_name : 문자열
        입력 파일 이름

    json_keys : 리스트
        형태소 분석 결과를 담고 있는 JSON 키의 리스트

    with_pos : 불리언
        True가 주어지면 품사를 /로 구분하여 붙여준다. (기본값: False)

    in_poses : 세트
        읽어들일 품사를 담고 있는 세트. (기본값: set())

    반환값
    ------
    docs : 리스트
        형태소 분석 문서들을 담고 있는 리스트
    """

    docs = []

    with open(input_file_name, "r", encoding="utf-8") as input_file:
        for line in input_file:
            json_doc = ujson.loads(line.strip())
            doc_morphs = []

            for json_key in json_keys:
                if json_key not in json_doc:
                    continue

                for sent_ma_res in json_doc[json_key]:
                    for morph_lex, morph_pos in sent_ma_res:
                        if in_poses and morph_pos not in in_poses:
                            continue

                        if with_pos:
                            doc_morphs.append(morph_lex + "/" + morph_pos)
                        else:
                            doc_morphs.append(morph_lex)

            doc = " ".join(doc_morphs)
            docs.append(doc)

    return docs



