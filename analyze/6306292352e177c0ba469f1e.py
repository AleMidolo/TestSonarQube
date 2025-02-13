def process_text_links(text):
    import re
    
    # Function to add attributes to a link
    def add_attributes(link):
        return f'<a href="{link}" target="_blank" rel="noopener noreferrer">{link}</a>'
    
    # Regex to find URLs in the text
    url_pattern = r'(https?://[^\s]+)'
    
    # Replace URLs with linkified versions
    text_with_links = re.sub(url_pattern, lambda match: add_attributes(match.group(0)), text)
    
    # Regex to find textual links (e.g., example.com)
    text_link_pattern = r'(?<!\w)([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(?!\w)'
    
    # Replace textual links with linkified versions
    final_text = re.sub(text_link_pattern, lambda match: add_attributes('http://' + match.group(1)), text_with_links)
    
    return final_text