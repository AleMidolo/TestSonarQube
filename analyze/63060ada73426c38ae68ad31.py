def _convert_non_cli_args(self, parser_name, values_dict):
    """
    तर्कों को सही प्रकारों में परिवर्तित करता है और values_dict पैरामीटर को संशोधित करता है।

    डिफ़ॉल्ट रूप से, सभी मान स्ट्रिंग्स के रूप में होते हैं।

    :param parser_name: कमांड का नाम, जैसे main, virsh, ospd, आदि।
    :param values_dict: तर्कों के साथ डिक्शनरी।
    """
    # Get parser configuration for this command
    parser_config = self.config.get(parser_name, {})
    
    # Iterate through arguments in values_dict
    for arg_name, value in values_dict.items():
        # Skip if value is None
        if value is None:
            continue
            
        # Get argument type from parser config
        arg_type = parser_config.get(arg_name, {}).get('type', str)
        
        try:
            # Convert boolean strings
            if arg_type == bool:
                if isinstance(value, str):
                    value = value.lower()
                    if value in ('true', 't', 'yes', 'y', '1'):
                        values_dict[arg_name] = True
                    elif value in ('false', 'f', 'no', 'n', '0'):
                        values_dict[arg_name] = False
                    
            # Convert numeric types        
            elif arg_type in (int, float):
                values_dict[arg_name] = arg_type(value)
                
            # Convert lists
            elif arg_type == list:
                if isinstance(value, str):
                    values_dict[arg_name] = value.split(',')
                    
        except (ValueError, TypeError):
            # Keep original value if conversion fails
            continue
            
    return values_dict