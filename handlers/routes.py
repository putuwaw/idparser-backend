from flask import request, jsonify
from flask_cors import cross_origin
from modules import modules, cyk
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

    @app.route("/parser", methods=['POST'])
    @cross_origin(origins=os.environ.get("CLIENT_URL"))
    def parser():
        requestString = request.get_json()
        string = requestString['string']
        result = cyk.is_accepted(string)
        tree = cyk.get_parse_tree(string)
        if (result):
            return jsonify({
                'result': True,
                'graph': tree.source
            })
        else:
            return jsonify({
                'result': False,
                'graph': None
            })
