from flask import Flask
from groq import prompts
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['GET'])
def home():
    content = prompts('''//binary search
    int binarySearch(int arr[], int low, int high, int x){
        while (low <= high) {
            int mid = low + (high - low) / 2;

            // Check if x is present at mid
            if (arr[mid] == x)
                return mid;
                ''')
    return content



if(__name__ == '__main__'):
    app.run()