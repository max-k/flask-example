# -*- encoding: utf-8; -*-

"""Application factory file"""

from flask import Flask, jsonify, request


def create_app(config):
    """Flask application factory"""

    app = Flask(__name__)
    app.config.from_object(config)

    @app.route('/')
    def hello_world():
        return 'Hello, world!'

    @app.route('/error')
    def zero_error():
        return 1/0

    @app.route('/json')
    def print_json():
        x = 0
        result = {}
        for arg in request.args:
            result[arg] = request.args.get(arg)
        return jsonify({'result': result})

    return app
