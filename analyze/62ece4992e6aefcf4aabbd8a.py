def load_configurations(config_filenames, overrides=None, resolve_env=True):
    """
    Dato un elenco di nomi di file di configurazione, carica e valida ciascun file di configurazione.
    Restituisci i risultati come una tupla composta da:
    - un dizionario che associa il nome del file di configurazione alla corrispondente configurazione analizzata,
    - una sequenza di istanze di `logging.LogRecord` contenenti eventuali errori di analisi.
    """
    import yaml
    import os
    import logging
    from collections import defaultdict
    
    # Initialize return values
    configs = {}
    errors = []
    logger = logging.getLogger(__name__)
    
    # Process each config file
    for filename in config_filenames:
        try:
            with open(filename, 'r') as f:
                # Load YAML content
                config = yaml.safe_load(f)
                
                # Resolve environment variables if requested
                if resolve_env:
                    config = _resolve_env_vars(config)
                
                # Apply overrides if provided
                if overrides:
                    config = _apply_overrides(config, overrides)
                    
                configs[filename] = config
                
        except (yaml.YAMLError, IOError) as e:
            # Log error and continue with next file
            error = logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=filename,
                lineno=0,
                msg=str(e),
                args=(),
                exc_info=None
            )
            errors.append(error)
            logger.error(f"Error loading config file {filename}: {str(e)}")
            
    return configs, errors

def _resolve_env_vars(config):
    """Helper function to resolve environment variables in config"""
    if isinstance(config, dict):
        return {k: _resolve_env_vars(v) for k, v in config.items()}
    elif isinstance(config, list):
        return [_resolve_env_vars(v) for v in config]
    elif isinstance(config, str) and config.startswith('${') and config.endswith('}'):
        env_var = config[2:-1]
        return os.environ.get(env_var, config)
    return config

def _apply_overrides(config, overrides):
    """Helper function to apply override values to config"""
    if isinstance(config, dict):
        result = config.copy()
        for k, v in overrides.items():
            if k in result and isinstance(result[k], dict) and isinstance(v, dict):
                result[k] = _apply_overrides(result[k], v)
            else:
                result[k] = v
        return result
    return config