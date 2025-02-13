import re
from re import Pattern

def _create_in_regex(self) -> Pattern:
    return re.compile(r'\b(?:in|not in)\s*\(\s*([^()]*)(?:\s*,\s*([^()]*))*\s*\)')