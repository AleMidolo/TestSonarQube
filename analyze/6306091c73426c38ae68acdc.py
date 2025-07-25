def validate_from_content(cls, spec_content=None):
    """
    validates that spec (YAML) content has all required fields

    :param spec_content: content of spec file
    :raise IRValidatorException: when mandatory data
    is missing in spec file
    :return: Dictionary with data loaded from a spec (YAML) file
    """
    import yaml

    required_fields = ['field1', 'field2', 'field3']  # Example required fields
    if spec_content is None:
        raise IRValidatorException("Spec content cannot be None")

    try:
        data = yaml.safe_load(spec_content)
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Error parsing YAML: {e}")

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise IRValidatorException(f"Missing mandatory fields: {', '.join(missing_fields)}")

    return data