#!/usr/bin/env python

from flask import Flask, request
from maltego import MaltegoMsg
from transforms import trx_getstastuscode


app = Flask(__name__)


@app.route('/', methods=['GET'])
def lambda_test():
    return 'Hello World'


@app.route('/tds/robots', methods=['GET', 'POST'])
def get_robots():
    return (trx_getstastuscode(MaltegoMsg(request.data)))


if __name__ == '__main__':
    app.run()
