import subprocess

from flask import Blueprint, Flask, jsonify, request, send_from_directory

api = Blueprint('api', __name__, url_prefix='/api/v1')

scripts_folder = 'scripts'
rabbit_filename = 'get_rabbit.sh'
mongo_filename = 'get_mongo.sh'
script_mimetype = 'application/x-sh'


@api.route("/get_rabbit")
def get_rabbit():
    return send_from_directory(
        scripts_folder, rabbit_filename, mimetype=script_mimetype)


@api.route("/get_mongo")
def get_mongo():
    return send_from_directory(
        scripts_folder, mongo_filename, mimetype=script_mimetype)


@api.route("/test_mongo")
def test_mongo():
    host = request.args.get('host')
    port = request.args.get('port')

    return_code = subprocess.call(
        "echo '' | mongo --host {} --port {} --quiet".format(host, port),
        shell=True)

    return jsonify({"success": return_code == 0})


app = Flask(__name__)
app.register_blueprint(api)
