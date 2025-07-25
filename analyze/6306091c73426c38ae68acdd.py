def validate_from_file(cls, yaml_file=None):
    """
    Carga y valida que un archivo YAML contenga todos los campos requeridos.

    :param yaml_file: Ruta al archivo YAML
    :raise IRValidatorException: cuando faltan datos obligatorios en el archivo
    :return: Diccionario con los datos cargados desde un archivo YAML
    """
    import yaml

    required_fields = cls.get_required_fields()  # Assuming this method exists in the class
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise IRValidatorException(f"Faltan los siguientes campos obligatorios: {', '.join(missing_fields)}")

    return data