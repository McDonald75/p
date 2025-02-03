from flask import request

from ..app import app
from .controllers import get_users, create_user, get_user

@app.route("/users", methods=['GET', 'POST'])
def list_create_accounts():
    if request.method == 'GET': return get_users()
    if request.method == 'POST': return create_user()
    else: return 'Method is Not Allowed'

@app.route("/users/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def retrieve_update_destroy_accounts(account_id):
    if request.method == 'GET': return get_user()
