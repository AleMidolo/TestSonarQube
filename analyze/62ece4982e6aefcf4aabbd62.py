def _replace_url_args(url, url_args):
    """
    किसी भी कस्टम स्ट्रिंग URL आइटम को `args` में दिए गए मानों से बदलें।
    
    :param url: URL स्ट्रिंग जिसमें कस्टम आइटम हो सकते हैं।
    :param url_args: एक डिक्शनरी जिसमें कस्टम आइटम और उनके मान होते हैं।
    :return: URL स्ट्रिंग जिसमें कस्टम आइटम को उनके मानों से बदल दिया गया है।
    """
    for key, value in url_args.items():
        url = url.replace(f"{{{key}}}", str(value))
    return url