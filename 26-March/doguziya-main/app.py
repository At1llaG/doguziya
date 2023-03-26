from flask import Flask, render_template, request, jsonify

#from flask_cors import CORS

from chat import get_response, get_id

app = Flask(__name__)
#CORS(app)

#"""
@app.get("/")
def index_get():
    return render_template("base.html")
#"""

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # check text validity #################
    response = get_response(text)
    
    id_value = get_id(text)
    message = {"answer": response, "id_value":id_value}
    return jsonify(message)



if __name__ == "__main__":
    app.run(debug=True)

