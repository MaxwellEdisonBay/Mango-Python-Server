from flask import Blueprint, render_template, send_file

index_bp = Blueprint('index_bp', __name__,
                     template_folder='templates',
                     static_folder='static', subdomain='www')


@index_bp.route("/static/<path:path>", subdomain="www")
def static_dir(path):
    return send_file("static/"+path)


@index_bp.route("/", methods=['POST', 'GET'], subdomain='www')
def main():
    return render_template("index.html")
