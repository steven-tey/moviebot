from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
from model import make_recommendation

# webapp
app = Flask(__name__, template_folder='./')

@app.route('/')
def main():
    return render_template('index.html')

@app.route("/get")
@cross_origin()
def get_recommendations():    
    userText = request.args.get('msg')    
    response =  make_recommendation(str(userText))
    return jsonify(response) 

if __name__ == '__main__':
    app.run(debug=True)
