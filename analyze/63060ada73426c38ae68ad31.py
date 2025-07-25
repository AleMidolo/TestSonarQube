def _convert_non_cli_args(self, parser_name, values_dict):
    """
    तर्कों को सही प्रकारों में परिवर्तित करता है और values_dict पैरामीटर को संशोधित करता है।

    डिफ़ॉल्ट रूप से, सभी मान स्ट्रिंग्स के रूप में होते हैं।

    :param parser_name: कमांड का नाम, जैसे main, virsh, ospd, आदि।
    :param values_dict: तर्कों के साथ डिक्शनरी।
    """
    if parser_name == "main":
        for key, value in values_dict.items():
            if value.isdigit():
                values_dict[key] = int(value)
            elif value.replace('.', '', 1).isdigit():
                values_dict[key] = float(value)
            elif value.lower() in ('true', 'false'):
                values_dict[key] = value.lower() == 'true'
    elif parser_name == "virsh":
        for key, value in values_dict.items():
            if key.endswith('_count'):
                values_dict[key] = int(value)
            elif key.endswith('_size'):
                values_dict[key] = float(value)
    elif parser_name == "ospd":
        for key, value in values_dict.items():
            if key.startswith('enable_'):
                values_dict[key] = value.lower() == 'true'
            elif key.startswith('max_'):
                values_dict[key] = int(value)
    # Add more parser-specific conversions as needed