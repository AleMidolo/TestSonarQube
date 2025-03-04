def validate_from_file(cls, yaml_file=None):
    """
    Carga y valida que un archivo YAML contenga todos los campos requeridos.

    :param yaml_file: Ruta al archivo YAML
    :raise IRValidatorException: cuando faltan datos obligatorios en el archivo 
    :return: Diccionario con los datos cargados desde un archivo YAML
    """
    try:
        import yaml
        
        if yaml_file is None:
            raise IRValidatorException("No se especificó un archivo YAML")
            
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)
            
        if not isinstance(data, dict):
            raise IRValidatorException("El archivo YAML debe contener un diccionario")
            
        required_fields = ['name', 'version', 'description']  # Campos requeridos ejemplo
        
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            raise IRValidatorException(f"Faltan los siguientes campos requeridos: {', '.join(missing_fields)}")
            
        return data
        
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Error al parsear el archivo YAML: {str(e)}")
    except FileNotFoundError:
        raise IRValidatorException(f"No se encontró el archivo: {yaml_file}")
    except Exception as e:
        raise IRValidatorException(f"Error inesperado: {str(e)}")

class IRValidatorException(Exception):
    pass