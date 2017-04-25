#!/usr/bin/python2.7
try:
    import json
    from ansible.plugins.callback import CallbackBase
except ImportError, ie:
    print str(ie)

class ResultCallback(CallbackBase):

    json = ''

    def v2_runner_on_failed(self, result, ignore_errors=False):
        self.json = json.dumps(result._result)

    def v2_runner_on_ok(self, result, **kwargs):
        self.json = json.dumps(result._result)