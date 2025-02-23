import yaml

class IRValidatorException(Exception):
    pass

def validate_from_file(cls, yaml_file=None):
    """
    एक YAML फ़ाइल को लोड और सत्यापित करता है कि उसमें सभी आवश्यक फ़ील्ड्स मौजूद हैं।

    :param yaml_file: YAML फ़ाइल का पथ
    :raise IRValidatorException: जब फ़ाइल में अनिवार्य डेटा गायब हो
    :return: YAML फ़ाइल से लोड किए गए डेटा के साथ एक डिक्शनरी
    """
    required_fields = cls.get_required_fields()  # Assuming this method exists in the class
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise IRValidatorException(f"Missing required fields: {', '.join(missing_fields)}")

    return data