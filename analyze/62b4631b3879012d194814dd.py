def fix_namespace_prefix_w(content):
    """
    ऐसा कोड लिखें जो उस टेक्स्ट को परिवर्तित करे जो डिफ़ॉल्ट रूप से 'w:st="' है, उसे 'w-st="' में बदल दे।
    """
    # Replace 'w:st="' with 'w-st="' in the content
    fixed_content = content.replace('w:st="', 'w-st="')
    return fixed_content