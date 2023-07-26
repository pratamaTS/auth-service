from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os
import routes 

load_dotenv()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600
app.register_blueprint(routes.bp)

jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(debug=True)