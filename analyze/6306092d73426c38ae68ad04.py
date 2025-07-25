def get_parser_option_specs(self, command_name):
    """
    निर्दिष्ट कमांड के लिए सभी विकल्प प्राप्त करता है।

    :param command_name: कमांड का नाम (जैसे main, virsh, ospd, आदि...)
    :return: सभी कमांड विकल्पों की सूची
    """
    # यहां हम मान लेते हैं कि कमांड विकल्पों की सूची एक डिक्शनरी में संग्रहीत है
    # जहां कुंजी कमांड नाम है और मान विकल्पों की सूची है
    command_options = {
        "main": ["--help", "--version", "--verbose"],
        "virsh": ["--connect", "--list", "--details"],
        "ospd": ["--config", "--log-level", "--output"]
    }
    
    # यदि कमांड नाम डिक्शनरी में मौजूद है, तो उसके विकल्पों की सूची लौटाएं
    if command_name in command_options:
        return command_options[command_name]
    else:
        # यदि कमांड नाम नहीं मिलता है, तो खाली सूची लौटाएं
        return []