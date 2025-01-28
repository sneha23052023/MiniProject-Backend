from flask import Flask
from groq import prompts
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['GET'])
def home():
    content = prompts("Program for binary search")
    return content



if(__name__ == '__main__'):
    app.run()