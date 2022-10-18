from flask import Flask, render_template, request, jsonify
#from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
#CORS(app)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
    
    
# from flask import Flask

#app = Flask(__name__)

#@app.route("/", methods=["GET"])
#def home():
#    return "Hello World!"
#if __name__ == "__main__":
#    app.run("0.0.0.0",5000)

#app.run(debug=False, port=5000, host='0.0.0.0')