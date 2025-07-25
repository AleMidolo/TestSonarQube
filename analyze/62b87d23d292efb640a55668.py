def get_config():
    """
    VersioneerConfig() ऑब्जेक्ट बनाएं, इसे डेटा से भरें और इसे लौटाएं।
    """
    class VersioneerConfig:
        def __init__(self):
            self.data = {}

        def add_data(self, key, value):
            self.data[key] = value

        def get_data(self):
            return self.data

    config = VersioneerConfig()
    # यहां आप डेटा को जोड़ सकते हैं, उदाहरण के लिए:
    config.add_data('version', '1.0.0')
    config.add_data('author', 'Your Name')
    
    return config