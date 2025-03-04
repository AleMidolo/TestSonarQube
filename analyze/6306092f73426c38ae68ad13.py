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
    
    # Add verbosity
    if verbose:
        if isinstance(verbose, bool):
            cmd.append('-v')
        elif isinstance(verbose, int):
            cmd.append('-' + 'v' * verbose)
            
    # Add inventory if workspace has one
    if hasattr(ir_workspace, 'inventory'):
        cmd.extend(['-i', ir_workspace.inventory])
        
    # Add extra vars
    if extra_vars:
        for key, value in extra_vars.items():
            cmd.extend(['--extra-vars', f'{key}={value}'])
            
    # Add any additional ansible arguments
    if ansible_args:
        for arg, value in ansible_args.items():
            if value is True:
                cmd.append(f'--{arg}')
            elif value is not False:
                cmd.extend([f'--{arg}', str(value)])
                
    # Execute the playbook
    try:
        result = subprocess.run(
            cmd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise Exception(f"Ansible playbook execution failed: {e.stderr}")