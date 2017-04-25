#!/usr/bin/python2.7
try:
    import bottle
    from bottle import post, request
    application = bottle.default_app()
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
    print '{"result": "' + str(i) + '"}'

@post('/post_data')
def post_data():
    try:
        run = api.Run()
        results_callback = '{"result": "'+run.start(request.body.read())+'"}'
    except Exception, ex1:
        results_callback = '{"result": "'+str(ex1)+'"}'

    print results_callback