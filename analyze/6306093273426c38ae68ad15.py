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
    from tempfile import NamedTemporaryFile

    # Create temporary file for vars
    with NamedTemporaryFile(mode='w', suffix='.json', delete=False) as vars_file:
        json.dump(vars_dict, vars_file)
        vars_file_path = vars_file.name

    try:
        # Build ansible-playbook command
        cmd = ['ansible-playbook']
        
        # Add any CLI arguments
        cmd.extend(cli_args)
        
        # Add vars file as extra vars
        cmd.extend(['-e', f'@{vars_file_path}'])
        
        # Add workspace inventory if exists
        if ir_workspace and hasattr(ir_workspace, 'inventory'):
            cmd.extend(['-i', ir_workspace.inventory])
            
        # Add plugin playbook path if exists  
        if ir_plugin and hasattr(ir_plugin, 'playbook_path'):
            cmd.append(ir_plugin.playbook_path)

        # Run ansible-playbook command
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            check=True
        )
        
        return result

    except subprocess.CalledProcessError as e:
        # Handle ansible errors
        raise Exception(f"Ansible playbook failed: {e.stderr}")
        
    finally:
        # Cleanup temp vars file
        if os.path.exists(vars_file_path):
            os.unlink(vars_file_path)