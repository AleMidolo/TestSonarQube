import re

def _get_resource_name_regex():
    pattern = r'^[a-zA-Z0-9-_]{1,63}$'
    return re.compile(pattern)