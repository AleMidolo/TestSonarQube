def ansible_playbook(ir_workspace, ir_plugin, playbook_path, verbose=None,
                     extra_vars=None, ansible_args=None):
    """
    'ansible-playbook' CLI को रैप करता है।

    :param ir_workspace: एक Infrared Workspace ऑब्जेक्ट जो सक्रिय वर्कस्पेस को दर्शाता है।
    :param ir_plugin: वर्तमान प्लगइन का एक InfraredPlugin ऑब्जेक्ट।
    :param playbook_path: वह प्लेबुक जिसे निष्पादित करना है।
    :param verbose: Ansible की वर्बोसिटी स्तर।
    :param extra_vars: dict। इसे Ansible को अतिरिक्त वेरिएबल्स (extra-vars) के रूप में पास किया जाता है।
    :param ansible_args: ansible-playbook के तर्कों का एक dict, जिसे सीधे Ansible तक पहुँचाने के लिए उपयोग किया जाता है।
    """
    import subprocess
    import json

    command = ['ansible-playbook', playbook_path]

    if verbose is not None:
        command.append(f'-v' * verbose)

    if extra_vars:
        for key, value in extra_vars.items():
            command.append(f'--extra-vars={key}={value}')

    if ansible_args:
        for key, value in ansible_args.items():
            command.append(f'--{key}={value}')

    result = subprocess.run(command, cwd=ir_workspace.path, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Ansible playbook failed: {result.stderr}")

    return json.loads(result.stdout)