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

    def v2_playbook_on_not_import_for_host(self, result, missing_file):
        self.data = result._result

    def v2_runner_on_unreachable(self, result):
        self.data = result._result

    def v2_runner_on_file_diff(self, result, diff):
        self.data = result._result

    def v2_runner_on_async_failed(self, result):
        self.data = result._result

    def v2_runner_item_on_ok(self, result):
        self.data = result._result

    def _clean_results(self, result, task_name):
        self.data = result._result

    def _handle_exception(self, result):
        self.data = result._result

    def v2_playbook_on_notify(self, result, handler):
        self.data = result._result

    def _process_items(self, result):
        self.data = result._result

    def _get_item(self, result):
        self.data = result._result

    def v2_runner_on_skipped(self, result):
        self.data = result._result

    def v2_playbook_on_import_for_host(self, result, imported_file):
        self.data = result._result

    def v2_runner_retry(self, result):
        self.data = result._result

    def v2_runner_on_async_ok(self, result):
        self.data = result._result

    def v2_runner_on_async_poll(self, result):
        self.data = result._result

    def v2_runner_item_on_failed(self, result):
        self.data = result._result

    def _dump_results(self, result, indent=None, sort_keys=True, keep_invocation=False):
        self.data = result._result

    def v2_runner_item_on_skipped(self, result):
        self.data = result._result
