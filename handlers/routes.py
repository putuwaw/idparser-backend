from flask import request, jsonify
from flask_cors import cross_origin
from modules import modules, cyk
import os

def configure_routes(app):
    @app.route("/")
    @cross_origin()
    def index():
        content = modules.content()
        return content

    @app.route("/parser", methods=['POST'])
    @cross_origin(origins=os.environ.get("CLIENT_URL"))
    def parser():
        requestString = request.get_json()
        string = requestString['string']
        result = cyk.is_accepted(string)
        tree = cyk.get_parse_tree(string)
        table = cyk.get_table_element(string)
        if (result):
            return jsonify({
                'result': True,
                'graph': tree.source,
                'table': table
            })
        else:
            return jsonify({
                'result': False,
                'graph': None,
                'table': table
            })
