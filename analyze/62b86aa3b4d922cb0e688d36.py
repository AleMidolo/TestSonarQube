import re
from typing import Dict, Any, List

class ValidationError(Exception):
    def __init__(self, messages: List[Dict[str, str]]):
        self.messages = messages
        super().__init__(str(messages))

def _validate_labels(labels: Dict[str, Any]) -> None:
    """
    Verifique que las claves y valores en las etiquetas dadas coincidan con sus expresiones regulares correspondientes.

    Argumentos:
    *labels (dict)*: las diferentes etiquetas a validar.

    Excepciones:
    *ValidationError*: si alguna de las claves o valores de las etiquetas no coincide con su respectiva expresión regular.
    """
    errors = []
    key_pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    value_pattern = re.compile(r'^[a-zA-Z0-9_]*$')

    for key, value in labels.items():
        # Validar la clave
        if not isinstance(key, str):
            errors.append({str(key): 'se esperaba un objeto de tipo cadena o bytes'})
        elif not key_pattern.match(key):
            errors.append({key: f"La clave de la etiqueta '{key}' no coincide con la expresión regular"})

        # Validar el valor
        if not isinstance(value, (str, bytes)):
            errors.append({str(value): 'se esperaba un objeto de tipo cadena o bytes'})
        elif isinstance(value, str) and not value_pattern.match(value):
            errors.append({value: f"El valor de la etiqueta '{value}' no coincide con la expresión regular"})

    if errors:
        raise ValidationError(errors)