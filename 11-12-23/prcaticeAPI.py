import flask
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def my_function():
    if request.method == 'GET':
        return jsonify({'CarName': 'Waganor', 'Company': 'MS', 'Model': '2017'})
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify({'CarName': '{}'.format(data['CarName']), 'company': '{}'.format(data['Company']),
                        'Model': '{}'.format(['Model'])})


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="80",debug=True)
