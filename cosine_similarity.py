#!/usr/bin/python3
#-*- coding: utf-8 -*-

from elasticsearch import Elasticksearch
from nltk import word_tokenize
from konlpy.tag import Kkma
from konlpy.utils import pprint

import sys
import re
import numpy

es_host="127.0.0.1"
es_port="9200"

es=Elasticsearch([{'host':es_host,'port':es_port}],timeout=30)

app=Flask(__name__)

#cosine 계산 함
def cos_similarity(v1,v2):
	dotpro=numpy.dot(v1,v2)
	norm=(numpy.linalg.norm(v1)*numpy.linalg.norm(v2))
	similarity=dotpro/norm

	return similarity

kkma=Kkma()
word_d={}
sent_list=[]

#먹고 싶은 음식 레시피 크롤링한 것 받아오기(리스트 만들기) =>합칠 때
def process_new_sentence(s):
	sent_list.append(s)
	tokenized=kkma.pos(s)
	for word in tokenized:
		if word not in word_d.keys():
			word_d[word]=0
		word_d[word]+=1

#엘라스틱 서치의 레시피 주요 단어 리스트 받아오기
#벡터 만들기 함수
def make_vector(i):
	v=[]
	s=sent_list[i]	
	tokenized=kkma.pos(s)
	for w in word_d.keys():
		val=0
		for t in tokenized:
			if t==w:
				val+=1
		v.append(val)
	return v
	
if __name__ == '__main__':
	#메인에서 for문을 돌려서 elasticsearch의 레시피 v1
	#//			먹고 싶은 음식에 대한 레시피 받아와서 v2
	#result=cos_similarity(v1,v2) #for문 돌려야 할 듯,,
	
	
