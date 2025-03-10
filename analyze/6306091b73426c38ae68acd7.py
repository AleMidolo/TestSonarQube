def ansible_config_manager(cls):
    """
    Ottiene il gestore di configurazione Ansible.
    """
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.callback import CallbackBase

    class ResultCallback(CallbackBase):
        """A sample callback plugin used for performing an action as results come in"""
        def v2_runner_on_ok(self, result, **kwargs):
            """Print a json representation of the result"""
            host = result._host
            print(f"{host.get_name()}: {result._result}")

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    callback = ResultCallback()

    return {
        'loader': loader,
        'inventory': inventory,
        'variable_manager': variable_manager,
        'callback': callback
    }