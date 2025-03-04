def validate_from_content(cls, spec_content=None):
    """
    validates that spec (YAML) content has all required fields

    :param spec_content: content of spec file
    :raise IRValidatorException: when mandatory data
    is missing in spec file
    :return: Dictionary with data loaded from a spec (YAML) file
    """
    if spec_content is None:
        raise IRValidatorException("No spec content provided")
        
    try:
        # Try to load YAML content
        import yaml
        yaml_content = yaml.safe_load(spec_content)
        
        if not isinstance(yaml_content, dict):
            raise IRValidatorException("Spec content must be a YAML dictionary")
            
        # Check for required fields
        required_fields = ['name', 'version', 'description']
        missing_fields = [field for field in required_fields if field not in yaml_content]
        
        if missing_fields:
            raise IRValidatorException(
                f"Missing mandatory fields in spec file: {', '.join(missing_fields)}"
            )
            
        # Additional validation can be added here
        # For example, checking field types, value ranges, etc.
        
        return yaml_content
        
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Invalid YAML content: {str(e)}")
    except Exception as e:
        raise IRValidatorException(f"Error validating spec content: {str(e)}")