from flask import Flask
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flask import current_app as app
from flask import request, jsonify

flask_Utils = Blueprint('flask_Utils', __name__,
                        template_folder='templates')


@flask_Utils.route('/echoJSON', methods=['POST', 'GET'])
def echoJSON():
    if request.method == 'POST':
        data = request.json
        return jsonify(data)
    else:
        return ""
#
# @flask_Utils.route('/', methods=['GET', 'POST'])
# def slash():
#     return render_template('index.html')


@flask_Utils.route('/myIP', methods=['GET', 'POST'])
def flask_myip():
    ip = 'Unknown Visitor'
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']  # if behind a proxy
    stmt = f'<html><body><h1>Hello</h1></body></html> {ip}'
    return stmt


@flask_Utils.route('/giveback', methods=['POST', 'GET'])
def giveback():
    d = []
    a = request.form
    for f in a:
        d.append(f)
    print(d)
    return d


@flask_Utils.route("/all-links")
def all_links():
    from flask import current_app

    links = []
    for rule in current_app.url_map.iter_rules():
        if rule is not None:
            links.append([rule.rule, rule.endpoint])
    return render_template("all_links.html", links=links)
