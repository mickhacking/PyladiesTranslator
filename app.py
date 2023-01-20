from flask import Flask, render_template, url_for, request, jsonify
from settings import HOST, PORT, DEBUG, THREADED, TOKEN
from requests import post

app = Flask(__name__)

@app.route("/hola-mundo")
def hola_mundo():
    return "Hola Mundo con Flask"

@app.route("/")
def index():
    styles = url_for("static", filename="css/styles.css")
    return render_template("index.html", styles=styles)

@app.route("/translator", methods=["POST"])
def translator():
    text = request.get_json().get("text")
    response = post(
        "https://duckduckgo.com/translation.js",
        params={
            "vqd": TOKEN,
            "query": "translate",
            "from": "es",
            "to": "en"
        },
        data=text
    )
    return jsonify(translate=response.json().get("translated"))




if __name__ == "__main__":
    app.run(HOST, PORT, DEBUG, threaded=THREADED)
