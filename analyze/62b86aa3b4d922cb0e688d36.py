import re

class ValidationError(Exception):
    def __init__(self, messages):
        self.messages = messages

def _validate_labels(labels):
    errors = []
    key_regex = r'^[a-zA-Z0-9_]+$'  # Example regex for keys
    value_regex = r'^[a-zA-Z0-9_]+$'  # Example regex for values

    for key, value in labels.items():
        if not isinstance(key, str) or not re.match(key_regex, key):
            errors.append({key: f"La clave de la etiqueta '{key}' no coincide con la expresión regular [...]"})
        
        if not isinstance(value, str):
            errors.append({str(value): 'se esperaba un objeto de tipo cadena o bytes'})
        elif not re.match(value_regex, value):
            errors.append({value: 'no coincide con la expresión regular [...]'})

    if errors:
        raise ValidationError(errors)