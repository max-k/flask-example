# -*- encoding: utf-8; -*-

import json
import pytest
from flask_example.__main__ import main


@pytest.fixture
def mon_app(monkeypatch):
    def _mon_app(param1=None, param2=None):
        if param1 is not None:
            monkeypatch.setenv('PARAM1', param1)
        if param2 is not None:
            monkeypatch.setenv('PARAM2', param2)
        return main(serve=False)
    return _mon_app


def test_root_entrypoint(mon_app):
    app = mon_app()
    client = app.test_client()
    assert client.get('/').data == b'Hello, world!'


def test_error_entrypoint(mon_app):
    app = mon_app()
    client = app.test_client()
    assert client.get('/error').status_code == 500


def test_json_entrypoint(mon_app):
    app = mon_app()
    client = app.test_client()
    data = json.loads(client.get('/json?arg1=arg1').data.decode('utf-8'))
    assert data == {'result': {'arg1': 'arg1'}}
