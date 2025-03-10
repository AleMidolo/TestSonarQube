import yaml

class IRValidatorException(Exception):
    pass

def validate_from_file(cls, yaml_file=None):
    """
    加载并验证一个 YAML 文件是否包含所有必需字段

    :param yaml_file: YAML 文件的路径
    :raise IRValidatorException: 当文件中缺少必需数据时抛出异常
    :return: 从 YAML 文件加载的数据字典
    """
    if yaml_file is None:
        raise IRValidatorException("YAML file path is required.")
    
    try:
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)
    except Exception as e:
        raise IRValidatorException(f"Failed to load YAML file: {e}")
    
    # Assuming the required fields are 'field1', 'field2', and 'field3'
    required_fields = ['field1', 'field2', 'field3']
    
    for field in required_fields:
        if field not in data:
            raise IRValidatorException(f"Missing required field: {field}")
    
    return data