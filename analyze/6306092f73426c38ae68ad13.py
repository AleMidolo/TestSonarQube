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
    import os
    import subprocess
    
    # Base command
    cmd = ['ansible-playbook', playbook_path]
    
    # Add verbosity if specified
    if verbose:
        if isinstance(verbose, bool):
            cmd.append('-v')
        elif isinstance(verbose, int):
            cmd.append('-' + 'v' * verbose)
            
    # Add extra vars if provided
    if extra_vars:
        if isinstance(extra_vars, dict):
            for key, value in extra_vars.items():
                cmd.extend(['--extra-vars', f'{key}={value}'])
                
    # Add inventory file from workspace if it exists
    if hasattr(ir_workspace, 'inventory'):
        inventory_path = ir_workspace.inventory
        if os.path.exists(inventory_path):
            cmd.extend(['-i', inventory_path])
            
    # Add any additional ansible arguments
    if ansible_args:
        if isinstance(ansible_args, dict):
            for key, value in ansible_args.items():
                if len(key) == 1:
                    cmd.append(f'-{key}')
                else:
                    cmd.append(f'--{key}')
                if value is not None:
                    cmd.append(str(value))
                    
    # Execute the ansible-playbook command
    try:
        result = subprocess.run(cmd, 
                              check=True,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        raise Exception(f"Ansible playbook execution failed: {e.stderr}")