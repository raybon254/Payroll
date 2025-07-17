from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager  # ✅ Add JWTManager
from models.conn import db  # ✅ Correct relative import
from models.routes import PayrollResource  # ✅ Adjusted import path
from models.login import Login  # ✅ Add Login endpoint
from models.register import Register  # ✅ Add Register endpoint
from models.refresh import TokenRefresh  # ✅ Add Refresh endpoint

app = Flask(__name__)

# ✅ App Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payroll.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # ✅ Required for JWT

# ✅ Initialize Extensions
db.init_app(app)
jwt = JWTManager(app)

# ✅ Setup Flask-Restful API
api = Api(app)

# ✅ Register API Resources
api.add_resource(Register, "/register")
api.add_resource(Login, "/login")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(PayrollResource, "/payroll")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # ✅ Ensure tables are created
    app.run(debug=True)
