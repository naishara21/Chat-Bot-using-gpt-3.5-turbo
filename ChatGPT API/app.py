from flask import Flask, render_template, request
import openai
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    message = request.json.get("message")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    if completion.choices[0].message:
        return completion.choices[0].message

    return 'Failed to generate response!'

if __name__ == '__main__':
    app.run()
