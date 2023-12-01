###  Assignment No 2 ###
#Name : Kiran Sanjay Lungade
#Batch : B2
#Roll No : 38
#Assignment Title : Bag of words and TFIDF

import numpy as np
from gensim.utils import simple_preprocess
from gensim import corpora
from gensim import models

text2 = open('kiranlungade.txt', encoding ='utf-8')
 
tokens2 =[]
for line in text2.read().split('.'):
  tokens2.append(simple_preprocess(line, deacc = True))

g_dict2 = corpora.Dictionary(tokens2)

print("The dictionary has: " +str(len(g_dict2)) + " tokens\n")
print(g_dict2.token2id)
g_bow =[g_dict2.doc2bow(token, allow_update = True) for token in tokens2]
print("\n Bag of Words : ", g_bow)
print("\n")
print("--------------------------------------------------------------------------------------")

print("--------------------------------------TFIDF VECTOR------------------------------------")


##TFIDF
text = [ "Our online English classes feature lots of useful learning materials."
        "Also activities to help you develop your reading skills."
        "It develop confidence in a safe and inclusive learning environment."
]

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])

g_tfidf = models.TfidfModel(g_bow, smartirs='ntc')

print("\n TF-IDF Vector:")
for item in g_tfidf[g_bow]:
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])


'''
**********    OUTPUT     ****************

The dictionary has: 26 tokens

{'classes': 0, 'english': 1, 'feature': 2, 'learning': 3, 'lots': 4, 'materials': 5, 'of': 6, 'online': 7, 'our': 8, 'useful': 9, 'activities': 10, 'also': 11, 'develop': 12, 'help': 13, 'reading': 14, 'skills': 15, 'to': 16, 'you': 17, 'your': 18, 'and': 19, 'confidence': 20, 'environment': 21, 'in': 22, 'inclusive': 23, 'it': 24, 'safe': 25}

 Bag of Words :  [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1)], [(10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1)], [(3, 1), (12, 1), (19, 1), (20, 1), (21, 1), (22, 1), (23, 1), (24, 1), (25, 1)], []]


--------------------------------------------------------------------------------------
--------------------------------------TFIDF VECTOR------------------------------------
Dictionary :
[['activities', 1], ['also', 1], ['and', 1], ['classes', 1], ['confidence', 1], ['develop', 2], ['english', 1], ['environment', 1], ['feature', 1], ['help', 1], ['in', 1], ['inclusive', 1], ['it', 1], ['learning', 2], ['lots', 1], ['materials', 1], ['of', 1], ['online', 1], ['our', 1], ['reading', 1], ['safe', 1], ['skills', 1], ['to', 1], ['useful', 1], ['you', 1], ['your', 1]]

 TF-IDF Vector:
[['activities', 0.18], ['also', 0.18], ['and', 0.18], ['classes', 0.18], ['confidence', 0.18], ['develop', 0.35], ['english', 0.18], ['environment', 0.18], ['feature', 0.18], ['help', 0.18], ['in', 0.18], ['inclusive', 0.18], ['it', 0.18], ['learning', 0.35], ['lots', 0.18], ['materials', 0.18], ['of', 0.18], ['online', 0.18], ['our', 0.18], ['reading', 0.18], ['safe', 0.18], ['skills', 0.18], ['to', 0.18], ['useful', 0.18], ['you', 0.18], ['your', 0.18]]

'''