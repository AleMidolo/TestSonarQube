def validate_from_file(cls, yaml_file=None):
    """
    加载并验证一个 YAML 文件是否包含所有必需字段

    :param yaml_file: YAML 文件的路径
    :raise IRValidatorException: 当文件中缺少必需数据时抛出异常
    :return: 从 YAML 文件加载的数据字典
    """
    import yaml

    required_fields = ['field1', 'field2', 'field3']  # 假设这些是必需字段

    if yaml_file is None:
        raise ValueError("YAML file path must be provided.")

    with open(yaml_file, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise IRValidatorException(f"Missing required fields: {', '.join(missing_fields)}")

    return data