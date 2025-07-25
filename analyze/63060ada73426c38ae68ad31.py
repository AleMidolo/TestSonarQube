def _convert_non_cli_args(self, parser_name, values_dict):
    """
    तर्कों को सही प्रकारों में परिवर्तित करता है और values_dict पैरामीटर को संशोधित करता है।

    डिफ़ॉल्ट रूप से, सभी मान स्ट्रिंग्स के रूप में होते हैं।

    :param parser_name: कमांड का नाम, जैसे main, virsh, ospd, आदि।
    :param values_dict: तर्कों के साथ डिक्शनरी।
    """
    # Get parser configuration for this command
    parser_config = self._get_parser_config(parser_name)
    
    if not parser_config:
        return
        
    # Iterate through arguments and convert types
    for arg_name, arg_config in parser_config.items():
        if arg_name in values_dict:
            arg_type = arg_config.get('type')
            
            # Convert value based on type
            if arg_type == 'bool':
                if isinstance(values_dict[arg_name], str):
                    values_dict[arg_name] = values_dict[arg_name].lower() in ('true', 't', 'yes', 'y', '1')
            elif arg_type == 'int':
                try:
                    values_dict[arg_name] = int(values_dict[arg_name])
                except (ValueError, TypeError):
                    pass
            elif arg_type == 'float':
                try:
                    values_dict[arg_name] = float(values_dict[arg_name]) 
                except (ValueError, TypeError):
                    pass
            elif arg_type == 'list':
                if isinstance(values_dict[arg_name], str):
                    values_dict[arg_name] = values_dict[arg_name].split(',')
            elif arg_type == 'dict':
                if isinstance(values_dict[arg_name], str):
                    try:
                        values_dict[arg_name] = eval(values_dict[arg_name])
                    except:
                        pass