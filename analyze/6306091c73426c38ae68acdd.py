import yaml

def validate_from_file(cls, yaml_file=None):
    """
    Carga y valida que un archivo YAML contenga todos los campos requeridos.

    :param yaml_file: Ruta al archivo YAML
    :raise IRValidatorException: cuando faltan datos obligatorios en el archivo
    :return: Diccionario con los datos cargados desde un archivo YAML
    """
    if yaml_file is None:
        raise ValueError("El archivo YAML no puede ser None.")
    
    try:
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo {yaml_file} no fue encontrado.")
    except yaml.YAMLError as e:
        raise ValueError(f"Error al cargar el archivo YAML: {e}")
    
    # Aquí puedes agregar la lógica de validación de campos obligatorios
    # Por ejemplo, si los campos obligatorios son 'name' y 'age':
    required_fields = ['name', 'age']
    for field in required_fields:
        if field not in data:
            raise IRValidatorException(f"Falta el campo obligatorio: {field}")
    
    return data

class IRValidatorException(Exception):
    pass