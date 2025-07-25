def validate_from_file(cls, yaml_file=None):
    """
    Loads & validates that a YAML file has all required fields

    :param yaml_file: Path to YAML file
    :raise IRValidatorException: when mandatory data is missing in file
    :return: Dictionary with data loaded from a YAML file
    """
    import yaml
    import os

    required_fields = ['field1', 'field2', 'field3']  # Example required fields

    if yaml_file is None or not os.path.isfile(yaml_file):
        raise FileNotFoundError("The specified YAML file does not exist.")

    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise IRValidatorException(f"Missing mandatory fields: {', '.join(missing_fields)}")

    return data