import os
import yaml

def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    Dato un nome di file di configurazione di destinazione e un file YAML di configurazione renderizzato, scrivilo nel file.  
    Crea eventuali directory contenitrici, se necessario. Tuttavia, se il file esiste già e `overwrite` è impostato su `False`, interrompi l'operazione prima di scrivere qualsiasi cosa.
    """
    # Controlla se il file esiste già
    if not overwrite and os.path.exists(config_filename):
        raise FileExistsError(f"Il file {config_filename} esiste già e overwrite è impostato su False.")
    
    # Crea le directory contenitrici se non esistono
    os.makedirs(os.path.dirname(config_filename), exist_ok=True)
    
    # Scrivi il file di configurazione
    with open(config_filename, 'w') as config_file:
        yaml.dump(rendered_config, config_file)
    
    # Imposta i permessi del file
    os.chmod(config_filename, mode)