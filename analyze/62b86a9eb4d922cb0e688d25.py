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
    # This pattern allows alphanumeric characters, hyphens, and underscores,
    # and ensures the name starts and ends with an alphanumeric character.
    pattern = r'^[a-zA-Z0-9]+([-_][a-zA-Z0-9]+)*$'
    return re.compile(pattern)