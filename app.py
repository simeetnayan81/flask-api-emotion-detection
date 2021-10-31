
import pickle
from flask import Flask, jsonify, request
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re
import pretoken
import __main__
__main__.preprocess_and_tokenize = pretoken.preprocess_and_tokenize

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def pred():
    message= request.args.get("message", None)
    filename = 'tfidf_svm.sav'
    model = pickle.load(open(filename, 'rb'))
    data=[message]
    emo = model.predict(data)
    result= {
        "message": message,
        "emotion": emo[0]
        }
    with app.app_context():
        jsonify(result)
    return result

if __name__=="__main__":
    app.run(debug=True)
