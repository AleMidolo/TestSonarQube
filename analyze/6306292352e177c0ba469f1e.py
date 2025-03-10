import re

def process_text_links(text):
    """
    Process links in text, adding some attributes and linkifying textual links.
    """
    # Regular expression to match URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    
    # Function to replace matched URLs with a link
    def linkify(match):
        url = match.group(0)
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'
    
    # Replace URLs in the text with the linkified version
    processed_text = url_pattern.sub(linkify, text)
    
    return processed_text