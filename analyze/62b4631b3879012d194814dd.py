def fix_namespace_prefix_w(content):
    # Replace 'w:st="' with 'w-st="' in the content
    return content.replace('w:st="', 'w-st="')