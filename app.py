from flask import Flask
app = Flask(__name__)

import routes 
app.register_blueprint(routes.bp)

if __name__ == '__main__':
    app.run(debug=True)