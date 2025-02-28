def _convert_non_cli_args(self, parser_name, values_dict):
    """
    तर्कों को सही प्रकारों में परिवर्तित करता है और values_dict पैरामीटर को संशोधित करता है।

    डिफ़ॉल्ट रूप से, सभी मान स्ट्रिंग्स के रूप में होते हैं।

    :param parser_name: कमांड का नाम, जैसे main, virsh, ospd, आदि।
    :param values_dict: तर्कों के साथ डिक्शनरी।
    """
    for key, value in values_dict.items():
        if isinstance(value, str):
            if value.lower() == 'true':
                values_dict[key] = True
            elif value.lower() == 'false':
                values_dict[key] = False
            elif value.isdigit():
                values_dict[key] = int(value)
            elif value.replace('.', '', 1).isdigit():
                values_dict[key] = float(value)
            elif value.lower() == 'none':
                values_dict[key] = None