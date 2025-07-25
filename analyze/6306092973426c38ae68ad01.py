def get_deprecated_args(self):
    """
    Restituzione di un dizionario con opzioni che deprecano altre.
    """
    deprecated_args = {
        'username': 'user',
        'passwd': 'password',
        'verbose': 'debug',
        'force': 'no_prompt',
        'old_format': 'format',
        'filename': 'file',
        'dest': 'destination',
        'src': 'source',
        'quiet': 'silent',
        'interactive': 'prompt'
    }
    return deprecated_args