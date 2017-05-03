#!/usr/bin/python2.7
try:
    from ansible.plugins.callback import CallbackBase
except (CallbackBase, ImportError), cie:
    print str(cie)


class ResultCallback(CallbackBase):

    data = ''

    def v2_runner_on_failed(self, result, ignore_errors=False):
        self.data = result._result

    def v2_runner_on_ok(self, result, **kwargs):
        self.data = result._result
