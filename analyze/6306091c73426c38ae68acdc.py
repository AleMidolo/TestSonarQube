def validate_from_content(cls, spec_content=None):
    """
    验证规范（YAML）内容是否包含所有必需字段。

    :param spec_content: 规范文件的内容
    :raise IRValidatorException: 当规范文件中缺少必需数据时抛出异常 
    :return: 从规范（YAML）文件加载的数据字典
    """
    if spec_content is None:
        raise IRValidatorException("规范内容不能为空")
        
    try:
        # 尝试加载YAML内容
        import yaml
        data = yaml.safe_load(spec_content)
        
        # 验证是否为字典
        if not isinstance(data, dict):
            raise IRValidatorException("规范内容必须是有效的YAML字典格式")
            
        # 检查必需字段
        required_fields = ['name', 'version', 'description']
        missing_fields = []
        
        for field in required_fields:
            if field not in data:
                missing_fields.append(field)
                
        if missing_fields:
            raise IRValidatorException(
                f"规范中缺少以下必需字段: {', '.join(missing_fields)}"
            )
            
        return data
        
    except yaml.YAMLError as e:
        raise IRValidatorException(f"无效的YAML格式: {str(e)}")
    except Exception as e:
        raise IRValidatorException(f"验证规范内容时发生错误: {str(e)}")