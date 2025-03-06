import re

def regex_dict(item):
    """
    Convert *.cpp keys to regex keys

    Given a dict where the keys are all filenames with wildcards, convert only
    the keys into equivalent regexes and leave the values intact.

    Example:

    rules = {
        '*.cpp':
            {'a': 'arf', 'b': 'bark', 'c': 'coo'},
        '*.h':
            {'h': 'help'}
    }
    regex_keys = regex_dict(rules)

    Args:
        item: dict to convert
    Returns:
        dict with keys converted to regexes
    """
    regex_dict = {}
    for key, value in item.items():
        # Convert the wildcard pattern to a regex pattern
        regex_pattern = re.escape(key).replace(r'\*', '.*')
        regex_dict[re.compile(regex_pattern)] = value
    return regex_dict