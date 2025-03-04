def get_config():
    """
    # VersioneerConfig() ऑब्जेक्ट बनाएं, इसे डेटा से भरें और इसे लौटाएं।
    """
    class VersioneerConfig:
        def __init__(self):
            self.VCS = "git"
            self.style = "pep440"
            self.tag_prefix = ""
            self.parentdir_prefix = "myproject-" 
            self.versionfile_source = "src/_version.py"
            self.versionfile_build = "myproject/_version.py"
            self.tag_regex = r"^v[0-9]+\.[0-9]+\.[0-9]+$"
            self.verbose = False
            self.update_files = True
            self.look_for_files = ["setup.py", "setup.cfg", "pyproject.toml"]
            self.allow_dirty = False
            self.git_describe_command = "git describe --tags --long --dirty --always"

    cfg = VersioneerConfig()
    return cfg