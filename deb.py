import numpy as np
import pickle
from flask import Flask, jsonify
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re

def preprocess_and_tokenize(data):

    #remove html markup
    data = re.sub("(<.*?>)", "", data)

    #remove urls
    data = re.sub(r'http\S+', '', data)

    #remove hashtags and @names
    data= re.sub(r"(#[\d\w\.]+)", '', data)
    data= re.sub(r"(@[\d\w\.]+)", '', data)

    #remove punctuation and non-ascii digits
    data = re.sub("(\\W|\\d)", " ", data)

    #remove whitespace
    data = data.strip()

    # tokenization with nltk
    data = word_tokenize(data)

    # stemming with nltk
    porter = PorterStemmer()
    stem_data = [porter.stem(word) for word in data]

    return stem_data


filename = 'tfidf_svm.sav'

model = pickle.load(open(filename, 'rb'))
message = 'delivery was hour late and my pizza is cold!'
pred = model.predict([message])
print(pred)
result= {
    "message": message,
    "emotion": pred[0]
    }

