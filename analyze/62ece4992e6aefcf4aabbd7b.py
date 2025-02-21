import os

def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    Dato un nome di file di configurazione di destinazione e un file YAML di configurazione renderizzato, scrivilo nel file.  
    Crea eventuali directory contenitrici, se necessario. Tuttavia, se il file esiste già e `overwrite` è impostato su `False`, interrompi l'operazione prima di scrivere qualsiasi cosa.
    """
    if not overwrite and os.path.exists(config_filename):
        raise FileExistsError(f"{config_filename} already exists and overwrite is set to False.")
    
    os.makedirs(os.path.dirname(config_filename), exist_ok=True)
    
    with open(config_filename, 'w') as config_file:
        config_file.write(rendered_config)
    
    os.chmod(config_filename, mode)