from typing import Tuple, Set
import re

def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    tags = set()
    def replacer_function(match):
        tag = match.group(1)
        tags.add(tag)
        return replacer(tag) if replacer else tag

    # Regex to find tags, ignoring those in code blocks
    pattern = r'(?<!`)(#\w+)(?!`)'
    modified_text = re.sub(pattern, replacer_function, text)
    
    return tags, modified_text