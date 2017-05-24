#!/usr/bin/python2.7
try:
    from ansible.plugins.callback import CallbackBase
except (CallbackBase, ImportError), cie:
    print str(cie)


class ResultCallback(CallbackBase):

    fields = ['cmd', 'command', 'msg', 'stdout_lines', 'stderr_lines', 'path', 'state']

    data = dict()

    def human_log(self, result):

        if type(result).isinstance(type(dict())):
            for field in self.fields:
                if field in result.keys():
                    self.data.update({field: result[field]})

    def v2_runner_on_failed(self, result, ignore_errors=False):
        self.human_log(result._result)

    def v2_runner_on_ok(self, result, **kwargs):
        self.human_log(result._result)

    def v2_playbook_on_not_import_for_host(self, result, missing_file):
        self.human_log(result._result)

    def v2_runner_on_unreachable(self, result):
        self.human_log(result._result)

    def v2_runner_on_file_diff(self, result, diff):
        self.human_log(result._result)

    def v2_runner_on_async_failed(self, result):
        self.human_log(result._result)

    def v2_runner_item_on_ok(self, result):
        self.human_log(result._result)

    def v2_playbook_on_notify(self, result, handler):
        self.human_log(result._result)

    def v2_runner_on_skipped(self, result):
        self.human_log(result._result)

    def v2_playbook_on_import_for_host(self, result, imported_file):
        self.human_log(result._result)

    def v2_runner_retry(self, result):
        self.human_log(result._result)

    def v2_runner_on_async_ok(self, result):
        self.human_log(result._result)

    def v2_runner_on_async_poll(self, result):
        self.human_log(result._result)

    def v2_runner_item_on_failed(self, result):
        self.human_log(result._result)

    def v2_runner_item_on_skipped(self, result):
        self.human_log(result._result)
