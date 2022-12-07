from flask import Flask
from flask_cors import CORS
from handlers.routes import configure_routes

app = Flask(__name__)
CORS(app)

configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
