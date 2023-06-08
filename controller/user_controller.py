from __main__ import app
from model.user_model import user_model
from flask import request

user = user_model()

@app.route("/user/getall")
def user_getall_controller():
    return user.user_getall_model()

@app.route("/user/add", methods = ["POST"])
def user_add_controller():
    return user.user_add_model(request.form)

@app.route("/user/update/<id>", methods = ["PUT"])
def user_update_controller(id):
    return user.user_update_model(request.form, id)

@app.route('/user/delete/<id>', methods=["DELETE"])
def user_delete_controller(id):
    return user.user_delete_model(id)