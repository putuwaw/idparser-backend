from flask import request, jsonify
from flask_cors import cross_origin
from modules import modules

def configure_routes(app):
    @app.route("/")
    @cross_origin()
    def index():
        hello = modules.hello()
        content = modules.content()
        return jsonify({"hello": hello, "content": content})

    @app.route("/test", methods=['POST'])
    @cross_origin()
    def test():
        requestString = request.get_json()
        temp = requestString['string']
        if (modules.is_palindrome(temp)):
            return jsonify({'result': 'String palindrome'})
        else:
            return jsonify({'result': 'String tidak palindrome'})
