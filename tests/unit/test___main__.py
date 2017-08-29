# -*- encoding: utf-8; -*-

import flask
from flask_example.__main__ import main


def test_main_function(monkeypatch):
    monkeypatch.setenv('PARAM2', 'param2')
    app = main(serve=False)
    assert isinstance(app, flask.Flask)
    assert app.config['PARAM1'] == 'param1'
    assert app.config['PARAM2'] == 0
    monkeypatch.setenv('PARAM2', '2')
    app = main(serve=False)
    assert app.config['PARAM2'] == 2
