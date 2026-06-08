from flask import Flask, render_template, request, jsonify
from scanner import scan_ports

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():

    data = request.get_json()

    target = data.get("ip")

    result = scan_ports(target)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)