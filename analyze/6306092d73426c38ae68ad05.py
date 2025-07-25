def get_option_spec(self, command_name):
    """
    दिए गए विकल्प नाम के लिए विनिर्देश प्राप्त करता है।
    """
    # यहाँ पर विकल्प विनिर्देश प्राप्त करने की लॉजिक लिखें
    option_spec = {}  # एक डिक्शनरी में विकल्प विनिर्देश संग्रहीत करें
    # उदाहरण के लिए, हम मान लेते हैं कि हम कुछ पूर्वनिर्धारित विकल्पों को वापस कर रहे हैं
    if command_name == "example_command":
        option_spec = {
            "option1": "Description for option 1",
            "option2": "Description for option 2",
        }
    return option_spec