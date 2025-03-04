def inject_config(self):
    """Set the environment variable for config path, if it is undefined."""
    if 'ANSIBLE_CONFIG' not in os.environ:
        os.environ['ANSIBLE_CONFIG'] = self.ansible_config_path