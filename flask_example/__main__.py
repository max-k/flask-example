#!/usr/bin/env python
# -*- encoding: utf-8; -*-

import os

from .app import create_app
from .config import Config


def main(serve=True):
    """Main entrypoint"""
    config = Config()

    config.PARAM1 = os.environ.get('PARAM1', 'param1')
    if 'PARAM2' in os.environ:
        try:
            config.PARAM2 = int(os.environ['PARAM2'])
        except ValueError:
            config.PARAM2 = 0

    app = create_app(config)

    if serve:
        app.run(debug=app.config.get('DEBUG', True))
    else:
        return app


if __name__ == '__main__':
    main()
