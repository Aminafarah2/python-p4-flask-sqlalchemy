from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable the modification tracking

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import your models to ensure they are registered with SQLAlchemy
from models import Owner, Pet

# Define your routes and other application logic here

if __name__ == '__main__':
    app.run(port=5555)
