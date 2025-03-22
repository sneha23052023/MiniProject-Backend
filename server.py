from flask import Flask,request
from groq import prompts
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['POST'])
def home():
    req = request.json
    hintType = req["hintType"]
    hintContent = req["hintContent"]
    content = prompts(hintType,hintContent)
    print(req)
    
    return content if content else " "



if(__name__ == '__main__'):
    app.run()