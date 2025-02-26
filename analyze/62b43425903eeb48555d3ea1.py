import re
from re import Pattern

def _create_in_regex(self) -> Pattern:
    """
    Create the in-style parameter regular expression.

    Returns the in-style parameter regular expression (:class:`re.Pattern`).
    """
    # Example regex pattern for in-style parameters, adjust as needed
    pattern = r'\b(?:in|not in)\s*\(\s*([^()]*?)\s*\)'
    return re.compile(pattern)