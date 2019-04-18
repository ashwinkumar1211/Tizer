# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 00:26:18 2019


"""

import xlrd 
import nltk
import nltk.classify.util
import nltk.classify
from sklearn.svm import LinearSVC
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

def word_feats(words):
    return dict([(word, True) for word in words])

issue = []
change = []
p1 = 0
p2 = 0
p3 = 0


loc1 = ("exc-rand.xlsx") 
  #using r to convert values to raw data format
wb1 = xlrd.open_workbook(loc1) 
sheet1 = wb1.sheet_by_index(0) 

for i in range(1,sheet1.nrows): 
    #print(sheet.cell_value(i, 2)) 
    set_e1 = (sheet1.cell_value(i, 0).lower(), sheet1.cell_value(i, 1))
    stopWords  = set(stopwords.words('english'))
    words = word_tokenize(set_e1[0])
    #here it'll give you the list of stopwords in english language
    #an empty list 
    for j in words:
        if j not in stopWords:
            change.append((j, set_e1[1]))  
            
            
         
def word_feats(words):
    return dict([(words, True)])


'''for entry in change:
    traindict = word_feats(entry[0])
    trainset.append((traindict, str(entry[1])))'''

trainset = [(word_feats(word[0]), word[1]) for word in change]
    
#issue_words = [(word_feats(iss), 'iss') for iss in issue]         

     
classifier = nltk.classify.SklearnClassifier(LinearSVC())
classifier.train(trainset)


wordz = []
sentence = "change my LAn immediately "
sentence = sentence.lower()
#words = sentence.split(' ')
stopWords  = set(stopwords.words('english'))
words = word_tokenize(sentence)
for j in words:
        if j not in stopWords:
            wordz.append(j) 
for word in wordz:
    classResult = classifier.classify(word_feats(word))
    if classResult == 1:
        p1 += 1
    if classResult == 2:
        p2 += 1
    if classResult == 3:
        p3 += 1
 
print(classResult)
print('P1: ' + str(float(p1)/len(wordz)))
print('P2: ' + str(float(p2)/len(wordz)))
print('P3: ' + str(float(p3)/len(wordz)))

#print('count',len(change))
