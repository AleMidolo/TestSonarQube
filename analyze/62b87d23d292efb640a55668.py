def get_config():
    """
    VersioneerConfig() ऑब्जेक्ट बनाएं, इसे डेटा से भरें और इसे लौटाएं।
    """
    class VersioneerConfig:
        def __init__(self):
            self.data = {}

        def fill_data(self, key, value):
            self.data[key] = value

        def get_data(self):
            return self.data

    config = VersioneerConfig()
    # Example data filling
    config.fill_data('version', '1.0.0')
    config.fill_data('author', 'Your Name')
    return config