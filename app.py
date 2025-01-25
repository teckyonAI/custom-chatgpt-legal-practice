from flask import Flask, render_template, request
from utils.drive_handler import search_drive
from utils.chatgpt_integration import generate_response
from utils.query_processor import process_query

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_query = request.form["query"]
        # Step 1: Search documents in Google Drive
        documents = search_drive(user_query)
        # Step 2: Process user query with ChatGPT
        response = generate_response(documents, user_query)
        return render_template("index.html", query=user_query, response=response)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
