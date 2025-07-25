import subprocess

def ansible_playbook(ir_workspace, ir_plugin, playbook_path, verbose=None, extra_vars=None, ansible_args=None):
    """
    'ansible-playbook' CLI को रैप करता है।

    :param ir_workspace: एक Infrared Workspace ऑब्जेक्ट जो सक्रिय वर्कस्पेस को दर्शाता है।
    :param ir_plugin: वर्तमान प्लगइन का एक InfraredPlugin ऑब्जेक्ट।
    :param playbook_path: वह प्लेबुक जिसे निष्पादित करना है।
    :param verbose: Ansible की वर्बोसिटी स्तर।
    :param extra_vars: dict। इसे Ansible को अतिरिक्त वेरिएबल्स (extra-vars) के रूप में पास किया जाता है।
    :param ansible_args: ansible-playbook के तर्कों का एक dict, जिसे सीधे Ansible तक पहुँचाने के लिए उपयोग किया जाता है।
    """
    command = ["ansible-playbook", playbook_path]

    if verbose:
        command.append(f"-{verbose}")

    if extra_vars:
        extra_vars_str = " ".join([f"{k}={v}" for k, v in extra_vars.items()])
        command.extend(["--extra-vars", extra_vars_str])

    if ansible_args:
        for key, value in ansible_args.items():
            command.append(f"--{key}")
            if value is not None:
                command.append(str(value))

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        raise