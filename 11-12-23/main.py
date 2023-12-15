# # import framework packeges
#
# import flask
# from flask import jsonify, Flask, request
#
#
#
# # creating object
#
# # app module
# app = Flask(__name__)
#
#
# @app.route('/', methods=['GET', 'POST'])
# def my_function():
#     if request.method == 'GET':
#         return jsonify({'message': 'Hello world' , 'name':'DLithe','DOB':'03-01-2000'})
#     elif request.method == 'POST':
#         data = request.get_json()
#         return jsonify({'message':'hello, {}'.format(data['name'])})
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
#
#
