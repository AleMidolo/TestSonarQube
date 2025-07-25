import re

def _get_resource_name_regex():
    """
    Build or return the regular expressions that are used to validate
    the name of the Krake resources.

    Returns:
        (re.Pattern): the compiled regular expressions, to validate
        the resource name.
    """
    # Example regex pattern for resource names: alphanumeric with underscores and hyphens
    pattern = r'^[a-zA-Z0-9_-]+$'
    return re.compile(pattern)