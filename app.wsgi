#!/usr/bin/python2.7
try:
    import json
    import bottle
    from bottle import post, request, response
    import ConfigParser
    config = ConfigParser.ConfigParser()
    import os
    import sys
    path = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, path)
    config.read(os.path.dirname(os.path.realpath(__file__))+'/config/app.ini')
    os.environ['ANSIBLE_CONFIG'] = config.get('DEFAULT', 'ANSIBLE_CONFIG')
    import api
except (ImportWarning, ImportError, Exception), i:
    result = json.dumps(str(i))

application = bottle.default_app()


@application.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = config.get('DEFAULT', 'ACCESS_CONTROL_ALLOW_ORIGIN')
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@application.post('/post_data')
def post_data():
    try:
        run = api.Run()
        result = json.dumps(run.start(request.body.read()))
    except Exception, ex1:
        result = json.dumps(str(ex1))

    return result

