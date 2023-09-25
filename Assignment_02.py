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
text = [ "NLP enables computers to understand natural language as humans do."
    "Whether the language is spoken or written,"
    "natural language processing uses artificial intelligence to take real-world input, process it,"
    "and make sense of it in a way a computer can understand."
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