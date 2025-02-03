from flask import request

from ..app import app
from .controllers import list_all_users_controller

@app.route("/users", methods=['GET', 'POST'])
def list_create_accounts():
    if request.method == 'GET': return list_all_users_controller()
    else: return 'Method is Not Allowed'

@app.route("/accounts/<account_id>", methods=['GET', 'PUT', 'DELETE'])
def retrieve_update_destroy_accounts(account_id):
    # if request.method == 'GET': return retrieve_account_controller(account_id)
    # if request.method == 'PUT': return update_account_controller(account_id)
    # if request.method == 'DELETE': return delete_account_controller(account_id)
    # else: rs //eturn 'Method is Not Allowed'
    pass
