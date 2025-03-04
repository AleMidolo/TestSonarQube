def validate_from_file(cls, yaml_file=None):
    """
    加载并验证一个 YAML 文件是否包含所有必需字段

    :param yaml_file: YAML 文件的路径 
    :raise IRValidatorException: 当文件中缺少必需数据时抛出异常
    :return: 从 YAML 文件加载的数据字典
    """
    try:
        import yaml
        
        if yaml_file is None:
            raise IRValidatorException("YAML file path cannot be None")
            
        # 读取YAML文件
        with open(yaml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            
        if not isinstance(data, dict):
            raise IRValidatorException("YAML file must contain a dictionary")
            
        # 验证必需字段
        required_fields = cls.get_required_fields()
        missing_fields = []
        
        for field in required_fields:
            if field not in data:
                missing_fields.append(field)
                
        if missing_fields:
            raise IRValidatorException(
                f"Missing required fields in YAML file: {', '.join(missing_fields)}"
            )
            
        return data
        
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Error parsing YAML file: {str(e)}")
    except FileNotFoundError:
        raise IRValidatorException(f"YAML file not found: {yaml_file}")
    except Exception as e:
        raise IRValidatorException(f"Unexpected error: {str(e)}")