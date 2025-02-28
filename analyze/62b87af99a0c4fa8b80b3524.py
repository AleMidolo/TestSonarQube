def is_run_el(obj):
    """
    ऑब्जेक्ट में 'run' नामक निष्पादन योग्य (executable) मेथड मौजूद है।
    """
    return callable(getattr(obj, 'run', None))