# -*- coding: utf-8 -*-
import csv
from konlpy.tag import Mecab
import gensim
from collections import namedtuple
import time

j=1
tmp_list=[]
doc_list=[]
main_str = str(0)
words = str(0)
csv_file = "C:/Users/int_sub05/.spyder-py3/sample/2017_01_0{}.csv"
csv_file2 = "C:/Users/int_sub05/.spyder-py3/sample/2017_01_{}.csv"
mecab = Mecab(dicpath="C:\mecab\mecab-ko-dic")
doc_vectorizer = gensim.models.Doc2Vec(
        dm=0,
        dbow_words=1,
        window=8,
        size=300,
        alpha=0.025,
        seed=1234,
        min_count=20,
        min_alpha=0.025,
        hs=1,
        negative=10)

for i in range(1,31):
    if i<=9:
        f = open(csv_file.format(i), 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            tmp_str = " ".join(line)
            main_str = main_str + tmp_str
            
            tok_article = mecab.morphs(line[2])
            class_name = [j]
            TaggedDocument = namedtuple('TaggedDocumnet', 'words tags')
            tagged_train_docs = TaggedDocument(tok_article, class_name)
            j=j+1
            doc_list.append(tagged_train_docs)
    else:
        f = open(csv_file2.format(i), 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            tmp_str = " ".join(line)
       
        main_str = main_str + tmp_str 
            
            tok_article = mecab.morphs(line[2])
            class_name = [j]
            TaggedDocument = namedtuple('TaggedDocumnet', 'words tags')
            tagged_train_docs = TaggedDocument(tok_article, class_name)
            j=j+1
            doc_list.append(tagged_train_docs)           
#Word2Vec#################################
str_split = main_str.split('.')
for i in range(0,len(str_split)):
    tok_str = mecab.morphs(str_split[i])
    tmp_list.append(tok_str)
model = gensim.models.Word2Vec(tmp_list)
model.save('model')
model=gensim.models.Word2Vec.load('model')
a=model.wv.most_similar("시스템")
#print(a)
##########################################
doc_vectorizer.build_vocab(doc_list)
print(str(doc_vectorizer))
# 벡터 문서 학습
start = time.time()
for epoch in range(10):
    doc_vectorizer.train(doc_list, total_examples=doc_vectorizer.corpus_count,
                         epochs=doc_vectorizer.iter)
    doc_vectorizer.alpha -= 0.002
    doc_vectorizer.min_alpha = doc_vectorizer.alpha
end = time.time()
print("During Time: {}".format(end-start))
# 학습된 doc2vec 모델 저장
model_name = 'Doc2Vec(dbow+w,d300,n10,hs,w8,mc20,s0.001,t3).model'
doc_vectorizer.save(model_name)
doc_vectorizer = gensim.models.Doc2Vec.load(model_name)
#print(doc_vectorizer.wv.most_similar('시스템'))
print(doc_vectorizer.docvecs[0])
f.close()