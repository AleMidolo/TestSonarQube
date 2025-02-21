def ansible_config_manager(cls):  
    """
    Ottiene il gestore di configurazione Ansible.
    """
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.display import Display
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    display = Display()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='path/to/inventory')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    return {
        'loader': loader,
        'inventory': inventory,
        'variable_manager': variable_manager,
        'display': display
    }