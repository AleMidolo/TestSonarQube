def validate_from_file(cls, yaml_file=None):
    """
    एक YAML फ़ाइल को लोड और सत्यापित करता है कि उसमें सभी आवश्यक फ़ील्ड्स मौजूद हैं।

    :param yaml_file: YAML फ़ाइल का पथ
    :raise IRValidatorException: जब फ़ाइल में अनिवार्य डेटा गायब हो 
    :return: YAML फ़ाइल से लोड किए गए डेटा के साथ एक डिक्शनरी
    """
    try:
        import yaml
        
        if yaml_file is None:
            raise IRValidatorException("YAML फ़ाइल का पथ प्रदान नहीं किया गया")
            
        with open(yaml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            
        if not isinstance(data, dict):
            raise IRValidatorException("YAML फ़ाइल एक वैध डिक्शनरी नहीं है")
            
        required_fields = ['name', 'version', 'description']  # आवश्यक फ़ील्ड्स की सूची
        
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            raise IRValidatorException(f"निम्नलिखित आवश्यक फ़ील्ड्स गायब हैं: {', '.join(missing_fields)}")
            
        return data
        
    except yaml.YAMLError as e:
        raise IRValidatorException(f"YAML फ़ाइल पार्स करने में त्रुटि: {str(e)}")
    except FileNotFoundError:
        raise IRValidatorException(f"फ़ाइल नहीं मिली: {yaml_file}")
    except Exception as e:
        raise IRValidatorException(f"अप्रत्याशित त्रुटि: {str(e)}")