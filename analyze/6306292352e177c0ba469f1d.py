from typing import Tuple, Set
import re

def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    tags = set()
    
    def replace_tag(match):
        tag = match.group(1)
        tags.add(tag)
        return replacer(tag) if replacer else tag

    # Regex to find tags, ignoring those inside code blocks
    pattern = r'(?<!`)(#\w+)(?!`)'
    replaced_text = re.sub(pattern, replace_tag, text)
    
    return tags, replaced_text