def validate_from_content(cls, spec_content=None):
    if not spec_content:
        raise IRValidatorException("Spec content cannot be empty")
        
    try:
        # Load YAML content into dictionary
        spec_dict = yaml.safe_load(spec_content)
        
        # Check if spec_dict is valid
        if not isinstance(spec_dict, dict):
            raise IRValidatorException("Invalid YAML format - must be a dictionary")
            
        # Check for required fields
        required_fields = ['name', 'version', 'description']
        missing_fields = []
        
        for field in required_fields:
            if field not in spec_dict:
                missing_fields.append(field)
                
        if missing_fields:
            raise IRValidatorException(f"Missing required fields: {', '.join(missing_fields)}")
            
        # Validate field types
        if not isinstance(spec_dict['name'], str):
            raise IRValidatorException("'name' field must be a string")
            
        if not isinstance(spec_dict['version'], (str, int, float)):
            raise IRValidatorException("'version' field must be a string or number")
            
        if not isinstance(spec_dict['description'], str):
            raise IRValidatorException("'description' field must be a string")
            
        return spec_dict
        
    except yaml.YAMLError as e:
        raise IRValidatorException(f"Invalid YAML format: {str(e)}")
    except Exception as e:
        raise IRValidatorException(f"Error validating spec content: {str(e)}")