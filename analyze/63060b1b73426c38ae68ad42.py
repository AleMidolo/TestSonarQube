def inject_config(self):
    import os
    if 'CONFIG_PATH' not in os.environ:
        os.environ['CONFIG_PATH'] = '/path/to/default/config'