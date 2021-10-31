
import pickle
from flask import Flask, jsonify, request
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re

def preprocess_and_tokenize(data):
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



app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def pred():
    message= request.args.get("message", None)
    filename = 'tfidf_svm.sav'
    model = pickle.load(open(filename, 'rb'))
    #message = 'delivery was hour late and my pizza is cold!'
    data=[message]
    pred = model.predict(data)
    result= {
        "message": message,
        "emotion": pred[0]
        }
    with app.app_context():
        jsonify(result)
    return result





if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)
