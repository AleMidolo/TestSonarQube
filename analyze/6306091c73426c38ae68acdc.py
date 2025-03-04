def validate_from_content(cls, spec_content=None):
    """
    Valida que el contenido del archivo spec (YAML) tenga todos los campos requeridos.

    :param spec_content: contenido del archivo spec
    :raise IRValidatorException: cuando faltan datos obligatorios
    en el archivo spec
    :return: Diccionario con los datos cargados desde un archivo spec (YAML)
    """
    if spec_content is None:
        raise IRValidatorException("El contenido del archivo spec no puede estar vacío")

    required_fields = ['name', 'version', 'description', 'author']
    
    for field in required_fields:
        if field not in spec_content:
            raise IRValidatorException(f"Campo requerido '{field}' no encontrado en el archivo spec")
            
    # Validaciones adicionales específicas
    if not isinstance(spec_content['version'], (str, int, float)):
        raise IRValidatorException("El campo 'version' debe ser un string o número")
        
    if not isinstance(spec_content['description'], str):
        raise IRValidatorException("El campo 'description' debe ser un string")
        
    if not isinstance(spec_content['author'], str):
        raise IRValidatorException("El campo 'author' debe ser un string")

    # Si todas las validaciones pasan, retornar el contenido validado
    return spec_content