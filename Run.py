#!/usr/bin/python2.7
try:
    import json
    import mysql.connector
    import os
    import ConfigParser
    config = ConfigParser.ConfigParser()
    if os.path.isfile(os.path.abspath(os.path.join(os.path.dirname(__file__), 'config')) + '/local/app.ini'):
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), 'config')) + '/local/app.ini')
    else:
        config.read(os.path.abspath(os.path.join(os.path.dirname(__file__), 'config')) + '/app.ini')
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ResultCallback import ResultCallback
except (ImportWarning, ImportError, Exception), i:
    print json.dumps(str(i))


class Run:

    def start(self, json_data):
        
        configMysql = ConfigParser.ConfigParser()
        configMysql.read(config.get('DEFAULT','DB_CONNECTION_FILE'))

        db = mysql.connector.connect(host=configMysql.get('INVENTORY','host'),
            user=configMysql.get('INVENTORY','user'),
            passwd=configMysql.get('INVENTORY','pass'),
            db=configMysql.get('INVENTORY','dbname'),
            charset='utf8mb4')

        cursor=db.cursor()
        get_hosts="select name from hosts"
        get_ips="select ip from hosts"
        cursor.execute(get_hosts)
        hosts=[item[0] for item in cursor.fetchall()]
        cursor.execute(get_ips)
        ips=[item[0] for item in cursor.fetchall()]

        data = {}

        data["hosts"] = hosts + ips
        # create play with tasks
        play_source = json.loads(json_data)

        Options = namedtuple('Options', ['module_path', 'forks', 'become', 'become_method', 'become_user', 'check'])

        # initialize needed objects
        variable_manager = VariableManager()
        loader = DataLoader()
        options = Options(module_path='/path/to/mymodules', forks=100, become=None,
                          become_method=None, become_user=None, check=False)
        passwords = dict(vault_pass='secret')

        # Instantiate our ResultCallback for handling results as they come in
        results_callback = ResultCallback()

        # create inventory and pass to var manager
        inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=data["hosts"])

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
                      stdout_callback=results_callback,
            )
            tqm.run(play)

        finally:
            if tqm is not None:
                tqm.cleanup()

        return results_callback.data
