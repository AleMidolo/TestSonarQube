def validate_from_content(cls, spec_content=None):
    """
    验证规范（YAML）内容是否包含所有必需字段。

    :param spec_content: 规范文件的内容
    :raise IRValidatorException: 当规范文件中缺少必需数据时抛出异常 
    :return: 从规范（YAML）文件加载的数据字典
    """
    if spec_content is None:
        raise IRValidatorException("Spec content cannot be None")
        
    try:
        # 尝试加载YAML内容
        import yaml
        data = yaml.safe_load(spec_content)
        
        # 检查data是否为字典
        if not isinstance(data, dict):
            raise IRValidatorException("Spec content must be a valid YAML dictionary")
            
        # 检查必需字段
        required_fields = ['name', 'version', 'description']
        missing_fields = []
        
        for field in required_fields:
            if field not in data:
                missing_fields.append(field)
                
        if missing_fields:
            raise IRValidatorException(
                f"Missing required fields in spec: {', '.join(missing_fields)}"
            )
            
        return data
        
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Invalid YAML content: {str(e)}")
    except Exception as e:
        raise IRValidatorException(f"Error validating spec content: {str(e)}")