def process_text_links(text):
    """
    Process links in text, adding some attributes and linkifying textual links.
    """
    import re

    # Function to add attributes to a link
    def add_attributes(match):
        url = match.group(0)
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'

    # Regular expression to find URLs in the text
    url_pattern = r'(https?://[^\s]+)'
    
    # Replace URLs in the text with linkified versions
    processed_text = re.sub(url_pattern, add_attributes, text)

    return processed_text