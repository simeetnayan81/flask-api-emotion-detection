from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re
import pickle

def preprocess_and_tokenize(data):
    data = re.sub("(<.*?>)", "", data)
    data = re.sub(r'http\S+', '', data)
    data= re.sub(r"(#[\d\w\.]+)", '', data)
    data= re.sub(r"(@[\d\w\.]+)", '', data)
    data = re.sub("(\\W|\\d)", " ", data)
    data = data.strip()
    data = word_tokenize(data)
    porter = PorterStemmer()
    stem_data = [porter.stem(word) for word in data]
    return stem_data
def mymod(message):
    filename = 'tfidf_svm.sav'
    model = pickle.load(open(filename, 'rb'))
    #message = 'delivery was hour late and my pizza is cold!'
    data=[message]
    pred = model.predict(data)
    return pred
