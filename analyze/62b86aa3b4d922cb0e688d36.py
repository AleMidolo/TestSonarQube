def _validate_labels(labels):
    import re
    from typing import Dict, Any

    # Expresión regular para validar claves de etiquetas
    KEY_REGEX = r'^[a-zA-Z][a-zA-Z0-9_-]*$'
    
    # Lista para almacenar los errores encontrados
    errors = []
    
    # Validar que labels sea un diccionario
    if not isinstance(labels, dict):
        raise ValidationError([{"labels": "se esperaba un diccionario"}])
        
    # Iterar sobre cada par clave-valor en las etiquetas
    for key, value in labels.items():
        
        # Validar que la clave sea una cadena
        if not isinstance(key, (str, bytes)):
            errors.append({
                str(key): 'se esperaba un objeto de tipo cadena o bytes'
            })
            continue
            
        # Validar que la clave coincida con la expresión regular
        if not re.match(KEY_REGEX, str(key)):
            errors.append({
                str(key): f"La clave de la etiqueta '{key}' no coincide con la expresión regular {KEY_REGEX}"
            })
            
        # Validar que el valor sea una cadena
        if not isinstance(value, (str, bytes)):
            errors.append({
                str(value): 'se esperaba un objeto de tipo cadena o bytes'
            })
            
    # Si hay errores, lanzar la excepción con todos los errores encontrados
    if errors:
        raise ValidationError(errors)

class ValidationError(Exception):
    def __init__(self, messages):
        self.messages = messages
        super().__init__(str(messages))