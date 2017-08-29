#!/usr/bin/env python
# -*- encoding: utf-8; -*-

"""
Setup file for flask_example
"""

from setuptools import setup

PKG_NAME = 'flask_example'


if __name__ == '__main__':
    setup(
        name=PKG_NAME,
        url='https://github.com/max-k/flask_example',
        description='Example flask application to use in Python demo',
        author='max-k',
        author_email='max-k@post.com',
        entry_points={
            'console_scripts':
                ['flask_example = {0}.__main__:main'.format(PKG_NAME)],
        },
        setup_requires=['pytest-runner'],
        tests_require=['pytest'],
        install_requires=['flask'],
        packages=[PKG_NAME]
    )
