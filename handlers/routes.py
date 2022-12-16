from flask import request, jsonify
from flask_cors import cross_origin
from modules import modules
import os

def configure_routes(app):
    @app.route("/")
    @cross_origin()
    def index():
        hello = modules.hello()
        content = modules.content()
        return jsonify({"hello": hello, "content": content})

    @app.route("/test", methods=['POST'])
    @cross_origin(origins=os.environ.get("CLIENT_URL"))
    def test():
        requestString = request.get_json()
        temp = requestString['string']
        graph = modules.draw_graph()
        if (modules.is_palindrome(temp)):
            return jsonify({
                'result': 'String palindrome', 
                'graph': graph.source,
            })
        else:
            return jsonify({
                'result': 'String tidak palindrome'
            })
