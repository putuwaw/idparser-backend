from flask import Flask, jsonify
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
        configure_routes(app)
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
