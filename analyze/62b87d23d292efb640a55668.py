def get_config():
    """
    VersioneerConfig() ऑब्जेक्ट बनाएं, इसे डेटा से भरें और इसे लौटाएं।
    """
    class VersioneerConfig:
        def __init__(self):
            self.data = {}

        def fill_data(self, **kwargs):
            self.data.update(kwargs)

    config = VersioneerConfig()
    config.fill_data(version="1.0.0", author="Your Name", description="Sample configuration")
    return config