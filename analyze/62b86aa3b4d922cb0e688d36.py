import re
from typing import Dict, Any, List

class ValidationError(Exception):
    def __init__(self, messages: List[Dict[str, str]]):
        self.messages = messages
        super().__init__(str(messages))

def _validate_labels(labels: Dict[str, Any]):
    errors = []
    
    # Expresión regular para validar claves de etiquetas
    key_regex = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    
    for key, value in labels.items():
        # Validar la clave
        if not isinstance(key, str) or not key_regex.match(key):
            errors.append({str(key): f"La clave de la etiqueta '{key}' no coincide con la expresión regular"})
        
        # Validar el valor
        if not isinstance(value, (str, bytes)):
            errors.append({str(value): 'se esperaba un objeto de tipo cadena o bytes'})
    
    if errors:
        raise ValidationError(errors)