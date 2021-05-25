from flask import Flask, json, request, render_template, jsonify
import uuid, json

app = Flask(__name__)

@app.route("/api", methods=["POST", "GET"])
def api_js():
    if request.method == 'POST':
        id = uuid.uuid4()
        name = request.get_json('name')
        comment = request.get_json('comments')
        return json.dumps({"name":name,"comment":comment})
    return render_template("showApi.html")

if __name__ == "__main__":
    app.run(debug=True)