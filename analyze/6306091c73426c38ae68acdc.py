import yaml

class IRValidatorException(Exception):
    pass

def validate_from_content(cls, spec_content=None):
    """
    यह फ़ंक्शन सत्यापित करता है कि spec (YAML) सामग्री में सभी आवश्यक फ़ील्ड्स मौजूद हैं।

    :param spec_content: spec फ़ाइल की सामग्री
    :raise IRValidatorException: जब spec फ़ाइल में अनिवार्य डेटा गायब हो
    :return: एक डिक्शनरी जिसमें spec (YAML) फ़ाइल से लोड किया गया डेटा होता है
    """
    if spec_content is None:
        raise IRValidatorException("Spec content is missing.")
    
    try:
        spec_data = yaml.safe_load(spec_content)
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Invalid YAML content: {e}")
    
    required_fields = ['field1', 'field2', 'field3']  # Replace with actual required fields
    
    for field in required_fields:
        if field not in spec_data:
            raise IRValidatorException(f"Missing required field: {field}")
    
    return spec_data