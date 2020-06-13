"""A Python Flask REST API Partner (CRUD) Style"""

from flask_cors import CORS, cross_origin
from routes import partner
import argparse
import logger_config
import os
from flask import Flask, jsonify, make_response

APP = Flask(__name__)
# Log setup
logger_config.configure_logger(APP, __name__)

# CORS setup
cors = CORS(APP)
APP.config['CORS_HEADERS'] = 'Content-Type'
APP.register_blueprint(partner.get_blueprint())


@APP.route("/")
@cross_origin()
def helloWorld():
    return "API - active"


@APP.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': str(_error)}), 400)


@APP.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@APP.errorhandler(409)
def handle_409_error(_error):
    """Return a http 409 error to client"""
    return make_response(jsonify({'error': 'Conflict'}), 409)


@APP.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)


if __name__ == '__main__':

    PARSER = argparse.ArgumentParser(
        description="Seans-Python-Flask-REST-Boilerplate")

    PARSER.add_argument('--debug', action='store_true',
                        help="Use flask debug/dev mode with file change reloading")
    ARGS = PARSER.parse_args()

    if ARGS.debug:
        print("Running in debug mode")
        APP.run(host='0.0.0.0', port=5000, debug=True)
    else:
        APP.run(host='0.0.0.0', port=5000, debug=False)
