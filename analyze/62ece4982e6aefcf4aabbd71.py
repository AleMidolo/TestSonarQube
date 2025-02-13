import re

def regex_dict(item):
    def convert_key_to_regex(key):
        # Escape special regex characters except for '*'
        key = re.escape(key).replace(r'\*', '.*')
        return f'^{key}$'  # Anchors the regex to match the whole string

    return {convert_key_to_regex(key): value for key, value in item.items()}