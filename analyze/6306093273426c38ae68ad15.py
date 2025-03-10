def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
    """
    使用 `vars` 字典运行 Ansible CLI。

    :param vars_dict: dict, 将作为 Ansible 的 extra-vars 传递
    :param cli_args: list, 命令行参数列表
    :param ir_workspace: 一个表示当前活动的工作区的Infrared Workspace 对象
    :param ir_plugin: 一个表示当前插件的InfraredPlugin 对象
    :return: ansible 的结果
    """
    from ansible.cli.playbook import PlaybookCLI
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    # 初始化 DataLoader
    loader = DataLoader()

    # 初始化 InventoryManager
    inventory = InventoryManager(loader=loader, sources=cli_args.get('inventory', None))

    # 初始化 VariableManager
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # 设置 extra-vars
    variable_manager.extra_vars = vars_dict

    # 初始化 PlaybookExecutor
    pbex = PlaybookExecutor(
        playbooks=cli_args.get('playbooks', []),
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        passwords={}
    )

    # 运行 playbook
    result = pbex.run()

    return result