# -*- coding: utf-8 -*-
"""
Thanks to the author Ruhan Sa, who is the TA of IR project 3 in Fall 2015
"""

import json
import urllib.request

qid = 1
with open('test_query.txt', encoding="utf-8") as f:
    for line in f:
        query = line.strip('\n').replace(':', '')
        query = urllib.parse.quote(query)
        inurl = 'http://54.203.220.188:8983/solr/vsm/select?fl=score,id&indent=on&q=' + query + '&rows=20&wt=json'
        IRModel = 'VSM'
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