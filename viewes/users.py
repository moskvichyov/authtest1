from flask import request
from flask_restx import Resource, Namespace
from marshmallow import Schema, fields
from flask import Flask

from helpers.decorators import auth_required, admin_required
from container import user_service

app = Flask(__name__)
user_ns = Namespace('users')


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        all_users = user_service.get_all()
        res = UserSchema(many=True).dump(all_users)
        return res, 200

    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):
    @admin_required
    def delete(self, uid):
        user_service.delete(uid)
        return "", 204


if __name__ == '__main__':
    app.run()