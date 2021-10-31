
import pickle
from flask import Flask, jsonify, request
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re
import pretoken

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def pred():
    message= request.args.get("message", None)
    emo=pretoken.mymod(message)
    result= {
        "message": message,
        "emotion": emo[0]
        }
    with app.app_context():
        jsonify(result)
    return result




if __name__=="__main__":
    from pretoken import preprocess_and_tokenize, mymod
    app.run()
