import os

def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    if not overwrite and os.path.exists(config_filename):
        raise FileExistsError(f"{config_filename} already exists and overwrite is False.")
    
    os.makedirs(os.path.dirname(config_filename), exist_ok=True)
    
    with open(config_filename, 'w') as config_file:
        config_file.write(rendered_config)
    
    os.chmod(config_filename, mode)