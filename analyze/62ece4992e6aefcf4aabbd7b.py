import os
import yaml

def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    Given a target config filename and rendered config YAML, write it out to file. Create any
    containing directories as needed. But if the file already exists and overwrite is False,
    abort before writing anything.
    """
    if os.path.exists(config_filename) and not overwrite:
        return
    
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(config_filename), exist_ok=True)
    
    # Write the rendered config to the file
    with open(config_filename, 'w') as f:
        yaml.dump(rendered_config, f)
    
    # Set the file permissions
    os.chmod(config_filename, mode)