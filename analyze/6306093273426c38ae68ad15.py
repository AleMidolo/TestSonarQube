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
    playbook_dir = os.path.join(ir_plugin.path, 'playbooks')
    inventory_file = os.path.join(ir_workspace.path, 'hosts')

    # एक्स्ट्रा वेरिएबल्स को JSON फाइल में लिखें
    extra_vars_file = os.path.join(ir_workspace.path, 'extra_vars.json')
    with open(extra_vars_file, 'w') as f:
        json.dump(vars_dict, f)

    # Ansible CLI कमांड तैयार करें
    ansible_cmd = ['ansible-playbook']
    ansible_cmd.extend(cli_args)
    ansible_cmd.extend([
        '-i', inventory_file,
        '--extra-vars', '@' + extra_vars_file
    ])

    # प्लेबुक को एक्जीक्यूट करें
    try:
        result = subprocess.run(
            ansible_cmd,
            cwd=playbook_dir,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Ansible execution failed: {e}")
        print(f"stdout: {e.stdout.decode()}")
        print(f"stderr: {e.stderr.decode()}")
        return e.returncode
    finally:
        # क्लीनअप - एक्स्ट्रा वेरिएबल्स फाइल हटाएं
        if os.path.exists(extra_vars_file):
            os.remove(extra_vars_file)