import yaml
from typing import Dict, Any

class IRValidatorException(Exception):
    pass

def validate_from_content(cls, spec_content=None) -> Dict[str, Any]:
    """
    Valida che il contenuto dello spec (YAML) contenga tutti i campi richiesti.

    :param spec_content: contenuto del file spec
    :raise IRValidatorException: quando i dati obbligatori
    sono mancanti nel file spec
    :return: Dizionario con i dati caricati da un file spec (YAML)
    """
    if spec_content is None:
        raise IRValidatorException("Il contenuto dello spec non può essere None.")
    
    try:
        spec_data = yaml.safe_load(spec_content)
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Errore nel parsing del contenuto YAML: {e}")
    
    required_fields = ["field1", "field2", "field3"]  # Esempio di campi obbligatori
    
    for field in required_fields:
        if field not in spec_data:
            raise IRValidatorException(f"Campo obbligatorio mancante: {field}")
    
    return spec_data