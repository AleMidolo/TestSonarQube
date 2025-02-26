import os
import yaml

def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    Given a target config filename and rendered config YAML, write it out to file. Create any
    containing directories as needed. But if the file already exists and overwrite is False,
    abort before writing anything.
    """
    # Create the containing directories if they do not exist
    os.makedirs(os.path.dirname(config_filename), exist_ok=True)
    
    # Check if the file already exists
    if not overwrite and os.path.exists(config_filename):
        raise FileExistsError(f"The file {config_filename} already exists and overwrite is set to False.")
    
    # Write the rendered config to the file
    with open(config_filename, 'w') as config_file:
        yaml.dump(rendered_config, config_file)
    
    # Set the file permissions
    os.chmod(config_filename, mode)