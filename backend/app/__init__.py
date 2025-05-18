from flask import Flask
from app.config import Config
from app.database import db
from app.auth import auth_bp

app = Flask(__name__)
app.config.from_object(Config)  # Load config
app.register_blueprint(auth_bp, url_prefix="")


db.init_app(app)
if __name__ == "__main__":
    app.run(debug=True)
