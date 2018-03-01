# -*- coding: utf-8 -*-
"""
Thanks to the author Ruhan Sa, who is the TA of IR project 3 in Fall 2015
"""

import json
import urllib.request

qid = 1
with open('queries1.txt', encoding="utf-8") as f:
    for line in f:
        query = line.strip('\n').replace(':', '')                
        query = urllib.parse.quote(query)     
        inurl = 'http://54.203.220.188:8983/solr/bm25/select?fl=score,id&defType=dismax&indent=on&q=' + query + '&qf=text_en_copy^5+text_de_copy^5+text_ru_copy^5+text_en_copyOther^5+text_de_copyOther^5+text_ru_copyOther^5+tweet_hashtags^1.2&pf=text_en_copy^5+text_de_copy^5+text_ru_copy^5+text_en_copyOther^5+text_de_copyOther^5+text_ru_copyOther^5+tweet_hashtags^1.2&rows=20&wt=json'
        IRModel = 'BM25'
        #outf = open(str(qid) + '.txt', 'a+')
        outf = open('Output_' + IRModel + '.txt', 'a+')
        data = urllib.request.urlopen(inurl).read()
        docs = json.loads(data.decode('utf-8'))['response']['docs']
        rank = 1
        for doc in docs:
            if qid < 10:
                outf.write('00' + str(qid) + ' ' + 'Q0 ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
            else:
                outf.write('0' + str(qid) + ' ' + 'Q0 ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')                
            rank += 1
        outf.close()
        qid += 1