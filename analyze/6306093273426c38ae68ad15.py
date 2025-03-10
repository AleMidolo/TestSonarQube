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

    # Convert vars_dict to JSON string for Ansible extra-vars
    extra_vars = json.dumps(vars_dict)

    # Prepare the Ansible command
    ansible_command = ['ansible-playbook'] + cli_args + ['-e', extra_vars]

    # Execute the Ansible command
    result = subprocess.run(ansible_command, capture_output=True, text=True)

    # Return the result
    return result