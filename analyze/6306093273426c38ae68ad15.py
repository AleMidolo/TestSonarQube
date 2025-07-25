def _run_playbook(cli_args, vars_dict, ir_workspace, ir_plugin):
    """
    Ansible CLI को vars_dict के साथ चलाता है।

    :param vars_dict: dict, इसे Ansible extra-vars के रूप में पास किया जाएगा
    :param cli_args: कमांड लाइन आर्ग्युमेंट्स की सूची
    :param ir_workspace: एक Infrared Workspace ऑब्जेक्ट जो सक्रिय वर्कस्पेस को दर्शाता है
    :param ir_plugin: वर्तमान प्लगइन का एक InfraredPlugin ऑब्जेक्ट
    :return: ansible के परिणाम
    """
    import subprocess
    import json

    # Prepare the command to run the Ansible playbook
    command = ['ansible-playbook'] + cli_args
    if vars_dict:
        extra_vars = json.dumps(vars_dict)
        command += ['--extra-vars', extra_vars]

    # Set the working directory to the Infrared workspace
    workspace_path = ir_workspace.path
    result = subprocess.run(command, cwd=workspace_path, capture_output=True, text=True)

    # Check for errors
    if result.returncode != 0:
        raise RuntimeError(f"Ansible playbook failed: {result.stderr}")

    return result.stdout