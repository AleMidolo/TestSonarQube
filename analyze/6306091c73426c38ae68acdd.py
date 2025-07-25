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
    if yaml_file is None:
        raise IRValidatorException("YAML फ़ाइल का पथ प्रदान नहीं किया गया है।")

    try:
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)
    except Exception as e:
        raise IRValidatorException(f"YAML फ़ाइल लोड करने में त्रुटि: {e}")

    # यहां आप आवश्यक फ़ील्ड्स की जांच कर सकते हैं
    required_fields = ['field1', 'field2', 'field3']  # उदाहरण के लिए आवश्यक फ़ील्ड्स
    for field in required_fields:
        if field not in data:
            raise IRValidatorException(f"अनिवार्य फ़ील्ड '{field}' YAML फ़ाइल में गायब है।")

    return data