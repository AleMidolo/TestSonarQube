import re

def _get_resource_name_regex():
    """
    Build or return the regular expressions that are used to validate
    the name of the Krake resources.

    Returns:
        (re.Pattern): the compiled regular expressions, to validate
        the resource name.
    """
    # Example regex pattern for resource names (adjust as needed)
    pattern = r'^[a-z0-9]([-a-z0-9]*[a-z0-9])?$'
    return re.compile(pattern)