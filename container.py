from dao.user import UserDAO
from services.user import UserService
from setup_db import db

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)