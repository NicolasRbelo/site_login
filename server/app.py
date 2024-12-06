from flask import *
from sqlalchemy import *
from flask_cors import CORS
from main import blueprint

app = Flask(__name__)
CORS(app)
app.register_blueprint(blueprint)

if __name__=="__main__":
    app.run(debug=True)