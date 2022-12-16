from flask import Flask, jsonify, request
from flask_cors import cross_origin
from modules import modules
from handlers.routes import configure_routes

def test_index():
    app = Flask(__name__)
    configure_routes(app)
    app.testing = True
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_api():
    app = Flask(__name__)
    with app.app_context():
        @app.route("/test", methods=['POST'])
        @cross_origin()
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
        app.testing = True
        client = app.test_client()
        response = client.post('/test', json={'string': 'katak'})
        assert response.status_code == 200
        assert response.get_json() == {
            "graph": "digraph G {\n\tHello -> World\n\tHello -> Halo\n\tWorld -> Dunia\n}\n",
            "result": "String palindrome"
        }
        response = client.post('/test', json={'string': 'kata'})
        assert response.status_code == 200
        assert response.get_json() == {'result': 'String tidak palindrome'}
