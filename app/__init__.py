from flask import Flask
from flask_login import LoginManager
from app.models import User, Session, create_db

app = Flask(__name__)
app.config["SECRET_KEY"] = "AprioriKS"

login_manager = LoginManager()
login_manager.login_view="login"
login_manager.init_app(app)

create_db()

@login_manager.user_loader
def load_user(user_id: int):
    with Session() as session:
        return session.query(User).where(User.id==user_id).first()