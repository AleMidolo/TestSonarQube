def validate_from_content(cls, spec_content=None):
    """
    यह फ़ंक्शन सत्यापित करता है कि spec (YAML) सामग्री में सभी आवश्यक फ़ील्ड्स मौजूद हैं।

    :param spec_content: spec फ़ाइल की सामग्री
    :raise IRValidatorException: जब spec फ़ाइल में अनिवार्य डेटा गायब हो
    :return: एक डिक्शनरी जिसमें spec (YAML) फ़ाइल से लोड किया गया डेटा होता है
    """
    import yaml

    required_fields = ['field1', 'field2', 'field3']  # अनिवार्य फ़ील्ड्स की सूची
    if spec_content is None:
        raise IRValidatorException("spec_content cannot be None")

    try:
        data = yaml.safe_load(spec_content)
    except yaml.YAMLError as e:
        raise IRValidatorException(f"YAML parsing error: {e}")

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise IRValidatorException(f"Missing required fields: {', '.join(missing_fields)}")

    return data