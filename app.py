from flask import Flask, jsonify, redirect, request
from flask_cors import CORS, cross_origin

from db.db import *

app = Flask(__name__)
CORS(app)


@app.route("/")
@cross_origin()
def hello_world():
    return redirect("http://www.github.com/conalli/bookshelf-client")


@app.route("/signup", methods=["POST"])
@cross_origin()
def sign_up():
    req = request.get_json()
    if len(req["name"]) < 3:
        return jsonify({"error": "username input: please use atleast 6 characters"})
    user = get_user_by_name(req["name"])
    if user is not None:
        return jsonify({"error": "username input: username already exists"})
    else:
        name = req["name"]
    if len(req["password"]) < 3:
        return jsonify({"error": "use password length greater than 3"})
    else:
        password = req["password"]
    id = add_user(name, password)

    resp = {"name": name, "password": password, "id": id}
    return jsonify(resp), 200


@app.route("/login", methods=["POST"])
@cross_origin()
def log_in():
    req = request.get_json()
    name = req["name"]
    password = req["password"]
    user = get_user_by_name_and_password(name, password)
    if user is not None:
        return jsonify({"login": True}), 200
    else:
        return jsonify({"login": False}), 404


@app.route("/setcmd", methods=["POST"])
@cross_origin()
def set_cmd():
    req = request.get_json()
    name = req["name"]
    password = req["password"]
    cmd = req["cmd"]
    url = req["url"]
    user = get_user_by_name_and_password(name, password)
    print(user)
    if user is not None:
        new_cmd = add_cmd(name, password, cmd, url)
        if new_cmd is not None:
            return jsonify({"new_cmds": new_cmd}), 200
        else:
            return jsonify({"error": "could not set command"}), 404
    else:
        return jsonify({"error": "could not find user"}), 404


@app.route("/getcmd", methods=["GET"])
@cross_origin()
def get_cmd():
    req = request.get_json()
    name = req["name"]
    password = req["password"]
    all_cmds = all_cmd(name, password)
    print(all_cmds)
    if all_cmds is not None:
        return jsonify(all_cmds), 200
    else:
        error = f"could not get commands for user -> {req[name]}"
        return jsonify({"error": error})


@app.route("/search/<name>/<password>/<cmd>", methods=["GET"])
@cross_origin()
def search(name, password, cmd):
    user_cmd = all_cmd(name, password)
    if user_cmd == None:
        return jsonify(
            {"error": "could not return find bookmarks for given name and password"}
        )
    if cmd in user_cmd:
        url = user_cmd[cmd]
        new_url = f"http://{url}"
        return redirect(new_url)
    else:
        new_url = f"http://www.google.com/search?q={cmd}"
        return redirect(new_url)
