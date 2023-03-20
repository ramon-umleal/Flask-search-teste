from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/search', methods=['POST'])
def search_cars():
    response = ""
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
