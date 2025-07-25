def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    Given a target config filename and rendered config YAML, write it out to file. Create any
    containing directories as needed. But if the file already exists and overwrite is False,
    abort before writing anything.
    """
    import os
    import pathlib

    # Get directory path and create if doesn't exist
    directory = os.path.dirname(config_filename)
    if directory:
        pathlib.Path(directory).mkdir(parents=True, exist_ok=True)

    # Check if file exists and overwrite flag
    if os.path.exists(config_filename) and not overwrite:
        return False

    # Write the configuration file with specified mode
    with open(config_filename, 'w') as f:
        os.chmod(config_filename, mode)
        f.write(rendered_config)
    
    return True