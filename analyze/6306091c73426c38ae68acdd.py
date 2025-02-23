def validate_from_file(cls, yaml_file=None):
    """
    Carga y valida que un archivo YAML contenga todos los campos requeridos.

    :param yaml_file: Ruta al archivo YAML
    :raise IRValidatorException: cuando faltan datos obligatorios en el archivo
    :return: Diccionario con los datos cargados desde un archivo YAML
    """
    import yaml
    from pathlib import Path

    required_fields = cls.get_required_fields()  # Assuming this method exists in the class
    if yaml_file is None:
        raise ValueError("El archivo YAML no puede ser None")

    yaml_path = Path(yaml_file)
    if not yaml_path.is_file():
        raise FileNotFoundError(f"El archivo {yaml_file} no existe")

    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise IRValidatorException(f"Faltan los siguientes campos obligatorios: {', '.join(missing_fields)}")

    return data