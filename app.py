
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def pred():
    message= request.args.get("message", None)
    result= {
        "message": message,
        "emotion": "Will do it too"
        }
    with app.app_context():
        jsonify(result)
    return result




if __name__=="__main__":
    app.run(threaded=True, port=5000)
