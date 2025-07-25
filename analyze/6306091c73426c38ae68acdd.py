def validate_from_file(cls, yaml_file=None):
    """
    加载并验证一个 YAML 文件是否包含所有必需字段

    :param yaml_file: YAML 文件的路径
    :raise IRValidatorException: 当文件中缺少必需数据时抛出异常
    :return: 从 YAML 文件加载的数据字典
    """
    import yaml

    required_fields = ['field1', 'field2', 'field3']  # 假设这些是必需字段

    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise IRValidatorException(f"缺少必需字段: {', '.join(missing_fields)}")

    return data