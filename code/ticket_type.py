# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 19:41:07 2019

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 23:54:22 2019

@author: user
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
iss = 0
cha = 0

loc = (r"D:\py - ticket\incident.xls") 
  #using r to convert values to raw data format
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
sheet.cell_value(0, 0) 
for i in range(sheet.nrows): 
    #print(sheet.cell_value(i, 2)) 
    set_e = sheet.cell_value(i, 2)
    stopWords  = set(stopwords.words('english'))
    words = word_tokenize(set_e)
    #here it'll give you the list of stopwords in english language
    #an empty list 
    for j in words:
        if j not in stopWords:
            issue.append(j)  
#print("\n",issue)

loc1 = (r"D:\py - ticket\change.xls") 
  #using r to convert values to raw data format
wb1 = xlrd.open_workbook(loc1) 
sheet1 = wb1.sheet_by_index(0) 
  
sheet1.cell_value(0, 0) 

set_e1 = []
for i in range(sheet1.nrows): 
    #print(sheet.cell_value(i, 2)) 
    set_e1 = sheet1.cell_value(i, 1)
    stopWords  = set(stopwords.words('english'))
    words = word_tokenize(set_e1)
    #here it'll give you the list of stopwords in english language
    #an empty list 
    for j in words:
        if j not in stopWords:
            change.append(j)  
#print("\n",change)



issue_words = [(word_feats(iss), 'iss') for iss in issue]
change_words = [(word_feats(cha), 'cha') for cha in change]

train_set = issue_words+change_words

classifier = nltk.classify.SklearnClassifier(LinearSVC())
classifier.train(train_set)

wordz = []
sentence = "mouse scroll not"
sentence = sentence.lower()
#words = sentence.split(' ')
stopWords  = set(stopwords.words('english'))
words = word_tokenize(sentence)
for j in words:
        if j not in stopWords:
            wordz.append(j) 
for word in wordz:
    classResult = classifier.classify(word_feats(word))
    if classResult == 'iss':
        iss = iss + 1
    if classResult == 'cha':
        cha = cha + 1
 
print('Issue: ' + str(float(iss)/len(wordz)))
print('Change: ' + str(float(cha)/len(wordz)))

#print('count',len(change))





 