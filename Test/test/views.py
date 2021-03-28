from flask import Flask, render_template, request, redirect, url_for
from .data import bdd as b
from .controller import traitement as t

app = Flask(__name__)
app.template_folder = "template"
app.static_folder = "static"
app.config.from_object('config')


@app.route("/")
def test():
    msg1, data1 = b.get_SynopsisData()
    print("views test: {0}".format(msg1))  # debug dans terminal
    return render_template("tab1.html", tab1=data1)


@app.route("/update_test", methods=['POST'])
def update_test():
    t.update_synopsis(request)
    return ""  # on ne retourne rien - tout est géré en javascript - pas de recharge de la page