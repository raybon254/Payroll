from flask import Flask
from flask_restful import Api
from payroll_resource import PayrollResource  # adjust import as needed

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your.db'  # or your DB URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from .conn import db
db.init_app(app)

api = Api(app)
api.add_resource(PayrollResource, "/payroll")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
