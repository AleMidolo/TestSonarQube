class VersioneerConfig:
    def __init__(self):
        self.version = None
        self.author = None
        self.license = None
        self.description = None

    def set_version(self, version):
        self.version = version

    def set_author(self, author):
        self.author = author

    def set_license(self, license):
        self.license = license

    def set_description(self, description):
        self.description = description

def get_config():
    """
    返回一个新的 `VersioneerConfig()` 对象，并设置其各种属性。
    创建、填充并返回 `VersioneerConfig()` 对象。
    """
    config = VersioneerConfig()
    config.set_version("1.0.0")
    config.set_author("Your Name")
    config.set_license("MIT")
    config.set_description("This is a sample project.")
    return config