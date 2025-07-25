def validate_from_file(cls, yaml_file=None):
    """
    Carica e valida che un file YAML contenga tutti i campi richiesti.

    :param yaml_file: Percorso del file YAML
    :raise IRValidatorException: quando mancano dati obbligatori nel file 
    :return: Dizionario con i dati caricati da un file YAML
    """
    try:
        import yaml
        
        if yaml_file is None:
            raise IRValidatorException("File YAML non specificato")
            
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)
            
        if not isinstance(data, dict):
            raise IRValidatorException("Il file YAML deve contenere un dizionario")
            
        required_fields = ['name', 'version', 'description']  # esempio campi richiesti
        
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            raise IRValidatorException(f"Campi obbligatori mancanti: {', '.join(missing_fields)}")
            
        return data
        
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Errore nel parsing del file YAML: {str(e)}")
    except FileNotFoundError:
        raise IRValidatorException(f"File non trovato: {yaml_file}")
    except Exception as e:
        raise IRValidatorException(f"Errore generico: {str(e)}")

class IRValidatorException(Exception):
    pass