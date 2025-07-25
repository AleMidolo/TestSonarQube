def validate_from_content(cls, spec_content=None):
    """
    验证规范（YAML）内容是否包含所有必需字段。

    :param spec_content: 规范文件的内容
    :raise IRValidatorException: 当规范文件中缺少必需数据时抛出异常
    :return: 从规范（YAML）文件加载的数据字典
    """
    import yaml
    from yaml import YAMLError

    if spec_content is None:
        raise IRValidatorException("Spec content cannot be None.")

    try:
        data = yaml.safe_load(spec_content)
    except YAMLError as e:
        raise IRValidatorException(f"Invalid YAML content: {e}")

    required_fields = ['field1', 'field2', 'field3']  # Replace with actual required fields

    for field in required_fields:
        if field not in data:
            raise IRValidatorException(f"Missing required field: {field}")

    return data