def _convert_non_cli_args(self, parser_name, values_dict):
    """
    तर्कों को सही प्रकारों में परिवर्तित करता है और values_dict पैरामीटर को संशोधित करता है।

    डिफ़ॉल्ट रूप से, सभी मान स्ट्रिंग्स के रूप में होते हैं।

    :param parser_name: कमांड का नाम, जैसे main, virsh, ospd, आदि।
    :param values_dict: तर्कों के साथ डिक्शनरी।
    """
    for key, value in values_dict.items():
        if isinstance(value, str):
            # Try to convert to int
            try:
                values_dict[key] = int(value)
                continue
            except ValueError:
                pass
            
            # Try to convert to float
            try:
                values_dict[key] = float(value)
                continue
            except ValueError:
                pass
            
            # Try to convert to boolean
            if value.lower() in ['true', 'false']:
                values_dict[key] = value.lower() == 'true'
                continue
            
            # Try to convert to list if the value is comma-separated
            if ',' in value:
                values_dict[key] = value.split(',')
                continue