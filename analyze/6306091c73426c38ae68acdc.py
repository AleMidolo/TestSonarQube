import yaml

class IRValidatorException(Exception):
    pass

def validate_from_content(cls, spec_content=None):
    """
    Valida que el contenido del archivo spec (YAML) tenga todos los campos requeridos.

    :param spec_content: contenido del archivo spec
    :raise IRValidatorException: cuando faltan datos obligatorios
    en el archivo spec
    :return: Diccionario con los datos cargados desde un archivo spec (YAML)
    """
    if spec_content is None:
        raise IRValidatorException("El contenido del archivo spec no puede ser None.")
    
    try:
        spec_data = yaml.safe_load(spec_content)
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Error al cargar el contenido YAML: {e}")
    
    required_fields = ["field1", "field2", "field3"]  # Ejemplo de campos requeridos
    
    for field in required_fields:
        if field not in spec_data:
            raise IRValidatorException(f"Falta el campo obligatorio: {field}")
    
    return spec_data