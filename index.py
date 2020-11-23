from flask import Flask, render_template, request, jsonify, make_response
import requests

# webapp
app = Flask(__name__, template_folder='./')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/get')
def get_from_api():
    query = request.args.get('msg')
    url = 'https://uitxgusnt5.execute-api.us-west-1.amazonaws.com/production/get?msg=' + query
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        print(e)