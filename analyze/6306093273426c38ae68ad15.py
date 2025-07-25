def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
    """
    Ansible CLI को vars_dict के साथ चलाता है।

    :param vars_dict: dict, इसे Ansible extra-vars के रूप में पास किया जाएगा 
    :param cli_args: कमांड लाइन आर्ग्युमेंट्स की सूची
    :param ir_workspace: एक Infrared Workspace ऑब्जेक्ट जो सक्रिय वर्कस्पेस को दर्शाता है
    :param ir_plugin: वर्तमान प्लगइन का एक InfraredPlugin ऑब्जेक्ट
    :return: ansible के परिणाम
    """
    import os
    import json
    import subprocess
    from ansible.cli import CLI
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    
    # Ansible के लिए आवश्यक डायरेक्टरी पथ सेट करें
    playbook_path = os.path.join(ir_plugin.path, 'playbooks')
    inventory_path = os.path.join(ir_workspace.path, 'hosts')
    
    # एक्स्ट्रा वेरिएबल्स को JSON में कन्वर्ट करें
    extra_vars = json.dumps(vars_dict)
    
    # Ansible CLI कमांड तैयार करें
    ansible_cmd = ['ansible-playbook']
    ansible_cmd.extend(cli_args)
    ansible_cmd.extend(['-i', inventory_path])
    ansible_cmd.extend(['--extra-vars', extra_vars])
    
    # Ansible के लिए आवश्यक ऑब्जेक्ट्स इनिशियलाइज़ करें
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=inventory_path)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    
    # प्लेबुक एग्जीक्यूटर सेटअप करें
    playbook = PlaybookExecutor(
        playbooks=[playbook_path],
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        options=CLI.base_parser().parse_args(ansible_cmd[1:]),
        passwords={}
    )
    
    try:
        # प्लेबुक चलाएं और परिणाम रिटर्न करें
        result = playbook.run()
        return result
    except Exception as e:
        print(f"Error running playbook: {str(e)}")
        return 1