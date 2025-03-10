import os
import yaml

def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    Dato un nome di file di configurazione di destinazione e un file YAML di configurazione renderizzato, scrivilo nel file.  
    Crea eventuali directory contenitrici, se necessario. Tuttavia, se il file esiste già e `overwrite` è impostato su `False`, interrompi l'operazione prima di scrivere qualsiasi cosa.
    """
    if os.path.exists(config_filename) and not overwrite:
        return
    
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(config_filename), exist_ok=True)
    
    # Write the rendered config to the file
    with open(config_filename, 'w') as config_file:
        yaml.dump(rendered_config, config_file, default_flow_style=False)
    
    # Set the file permissions
    os.chmod(config_filename, mode)