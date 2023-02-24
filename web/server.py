from flask import Flask, render_template, request
from .controllers.api_Controller_1 import resp
from .controllers.login_Controller import isLogin
from .controllers.uniport_api_call_1 import (
    get_uniport_primary_details,
    get_uniport_target_component_synonyms,
)

server = Flask(__name__)


@server.route("/")
def index():
    return render_template("index.html")


@server.route("/login", methods=["GET"])
def login():
    params = request.args
    u_name = params.get("username")
    p_name = params.get("password")
    login = isLogin(u_name, p_name)
    if login:
        return "Login Success"
    return render_template("login.html")


@server.route("/register")
def register():
    return render_template("register.html")


@server.route("/table_1")
def table_page_1():
    return render_template("table_1.html", response=resp, headers=resp[0].keys())


@server.route("/form")
def form():
    return render_template("form.html")


@server.route("/uniport", methods=["GET"])
def uniport_describe():
    params = request.args
    uniport_id = params.get("uniport_id")
    uniport_primary_details = get_uniport_primary_details(uniport_id)
    uniport_target_component_synonyms = get_uniport_target_component_synonyms(
        uniport_id
    )
    return render_template(
        "uniport_describe.html",
        uniport_id=uniport_id,
        primary=uniport_primary_details,
        syn=uniport_target_component_synonyms,
    )


@server.route("/showSelectedUniport")
def showSelectedUniport():
    str = ""
    params = request.args
    for key, value in params.items():
        # print(key, value)
        # print(value)
        str = str + " " + value + " "
    return "HelooWorld" + "<br/>" + "Selected values are -" + str


if __name__ == "__main__":
    server.jinja_env.auto_reload = True
    server.config["TEMPLATES_AUTO_RELOAD"] = True
    server.run(port="8080", host="0.0.0.0", debug=True)
