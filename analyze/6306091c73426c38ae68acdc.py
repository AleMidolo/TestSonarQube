def validate_from_content(cls, spec_content=None):
    """
    验证规范（YAML）内容是否包含所有必需字段。

    :param spec_content: 规范文件的内容
    :raise IRValidatorException: 当规范文件中缺少必需数据时抛出异常
    :return: 从规范（YAML）文件加载的数据字典
    """
    import yaml
    from yaml import YAMLError

    required_fields = ['field1', 'field2', 'field3']  # 示例必需字段

    if spec_content is None:
        raise IRValidatorException("规范内容不能为空")

    try:
        data = yaml.safe_load(spec_content)
    except YAMLError as e:
        raise IRValidatorException(f"YAML解析错误: {e}")

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise IRValidatorException(f"规范文件中缺少以下必需字段: {', '.join(missing_fields)}")

    return data