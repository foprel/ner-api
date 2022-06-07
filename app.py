from flask import Flask, jsonify, request, abort, make_response
from account_match import get_accounts, get_stopwords, match
import jwt
import datetime
import os
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['USER_NAME'] = os.environ.get('USER_NAME')
app.config['PASSWORD'] = os.environ.get('PASSWORD')
app.config['IP_RANGES'] = os.environ.get('IP_RANGE') #.split(",")

filename = "entity_names.csv"
accounts = get_accounts(filename)
stopwords = get_stopwords(filename)


def validate_token(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get("token")
        if not token:
            return jsonify({"message": "Token required!"}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except Exception:
            return jsonify({"message": "Token is invalid!"}), 403
        return func(*args, **kwargs)
    return decorated


def validate_ip(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        if not ip:
            return jsonify({"message": "Unable to identify ip address"}), 403
        try:
            if ip not in app.config["IP_RANGES"]:
                raise Exception("Ip address is invalid")
        except Exception:
            return jsonify({"message": "Ip address is invalid"}), 403
        return func(*args, **kwargs)
    return decorated


@app.route('/login', methods=['GET'])
def login():
    auth = request.authorization
    if auth and auth.password == app.config['PASSWORD'] and auth.username == app.config['USER_NAME']:
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=365)}, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})


@app.route('/api/account_name_client/', methods=['POST'])
@validate_token
def account_name_client():
    if not request.json.get("account_name_client"):
        abort(400)
    account_name_client = request.json.get("account_name_client")
    account_name_client_norm = match(account_name_client, accounts, stopwords, u=95, keep_old_value=True)
    print(f"{account_name_client} --> {account_name_client_norm}")
    return jsonify({
        "accountNameClient": account_name_client_norm
    })