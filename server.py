from flask import Flask
from groq import prompts


app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    content = prompts("Program for binary search")
    return content



if(__name__ == '__main__'):
    app.run()