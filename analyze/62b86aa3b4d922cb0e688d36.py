import re
from typing import Dict, List, Union

class ValidationError(Exception):
    def __init__(self, messages: List[Dict[str, str]]):
        self.messages = messages
        super().__init__(str(messages))

def _validate_labels(labels: Dict[str, Union[str, List[str]]]) -> None:
    """
    Verifica che le chiavi e i valori nelle etichette fornite corrispondano alle rispettive espressioni regolari.

    ### Argomenti:
    - **labels (dict)**: il dizionario contenente le diverse etichette da validare.

    ### Eccezioni:
    - **ValidationError**: viene sollevata se una qualsiasi delle chiavi o dei valori delle etichette non corrisponde alla rispettiva espressione regolare. L'errore contiene come messaggio la lista di tutti gli errori che si sono verificati nelle etichette. Ogni elemento della lista è un dizionario con una coppia chiave-valore:
      - **key**: la chiave dell'etichetta o il valore dell'etichetta per cui si è verificato un errore, come stringa.
      - **value**: il messaggio di errore.
    """
    key_regex = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    value_regex = re.compile(r'^[a-zA-Z0-9_]+$')
    errors = []

    for key, value in labels.items():
        # Validate key
        if not isinstance(key, str):
            errors.append({str(key): 'expected string or bytes-like object'})
        elif not key_regex.match(key):
            errors.append({key: f"Label key '{key}' does not match the regex {key_regex.pattern}"})

        # Validate value
        if isinstance(value, list):
            for item in value:
                if not isinstance(item, str):
                    errors.append({str(item): 'expected string or bytes-like object'})
                elif not value_regex.match(item):
                    errors.append({item: f"Label value '{item}' does not match the regex {value_regex.pattern}"})
        else:
            if not isinstance(value, str):
                errors.append({str(value): 'expected string or bytes-like object'})
            elif not value_regex.match(value):
                errors.append({value: f"Label value '{value}' does not match the regex {value_regex.pattern}"})

    if errors:
        raise ValidationError(errors)