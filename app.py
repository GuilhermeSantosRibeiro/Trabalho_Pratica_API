from flask import Flask
from routes import init_routs

app = Flask(__name__)
init_routs(app)

if __name__ == "__main__":
    app.run(debug=True)