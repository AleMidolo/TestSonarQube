import re
from re import Pattern

def _create_in_regex(self) -> Pattern:
    """
    Create the in-style parameter regular expression.

    Returns the in-style parameter regular expression (:class:`re.Pattern`).
    """
    # Example regex pattern for in-style parameters (e.g., "value1,value2,value3")
    pattern = r'^(?:[^,]+(?:,[^,]+)*)?$'
    return re.compile(pattern)