try:
    import json
    import os
    import ConfigParser
    config = ConfigParser.ConfigParser()
    config.read(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'config'))+'/app.ini')
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ResultCallback import ResultCallback
except (ImportWarning, ImportError, Exception), i:
    print str(i)


class Run:
    def start(self, json_data):

        Options = namedtuple('Options',
                             ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check'])
        # initialize needed objects
        variable_manager = VariableManager()
        loader = DataLoader()
        options = Options(connection='ssh', module_path='/path/to/mymodules', forks=100, become=False,
                          become_method='', become_user='', check=False)
        passwords = dict(vault_pass='secret')

        # Instantiate our ResultCallback for handling results as they come in
        results_callback = ResultCallback()

        # create inventory and pass to var manager
        inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=config.get('DEFAULT', 'HOST_LIST'))
        variable_manager.set_inventory(inventory)

        # create play with tasks
        play_sources = json.loads(json_data)

        for play_source in play_sources:

            play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

            # actually run it
            tqm = None
            try:
                tqm = TaskQueueManager(
                          inventory=inventory,
                          options=options,
                          passwords=passwords,
                          loader=loader,
                          variable_manager=variable_manager,
                          stdout_callback=results_callback,  # Use our custom callback instead of the ``default`` callback plugin
                )
                tqm.run(play)

            finally:
                if tqm is not None:
                    tqm.cleanup()

        return results_callback.json