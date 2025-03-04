def get_deprecated_args(self):
    """
    Restituzione di un dizionario con opzioni che deprecano altre.
    """
    deprecated_args = {
        'username': 'user',
        'passwd': 'password',
        'verbose': 'debug',
        'force': 'no_prompt',
        'quiet': 'silent',
        'file': 'filename',
        'dir': 'directory',
        'dest': 'destination',
        'src': 'source',
        'old': 'legacy'
    }
    return deprecated_args