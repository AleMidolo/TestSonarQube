def get_logical_path_map(inventory, version):
    """
    इन्वेंटरी में दिए गए संस्करण (version) के लिए स्थिति (state) में लॉजिकल पथों और डिस्क पर फ़ाइलों के बीच का मैप प्राप्त करें।

    रिटर्न करता है एक डिक्शनरी: 
    `logical_path_in_state -> set(content_files)`

    `content_files` का सेट उन डुप्लिकेट फ़ाइलों के संदर्भ भी शामिल कर सकता है जो उस संस्करण के बाद के संस्करणों में मौजूद हैं जिसे वर्णित किया जा रहा है।
    """
    logical_path_map = {}
    
    for item in inventory:
        if item['version'] == version:
            logical_path = item['logical_path']
            content_files = set(item['content_files'])
            logical_path_map[logical_path] = logical_path_map.get(logical_path, set()).union(content_files)
    
    # Include duplicates from later versions
    for item in inventory:
        if item['version'] > version:
            logical_path = item['logical_path']
            content_files = set(item['content_files'])
            if logical_path in logical_path_map:
                logical_path_map[logical_path] = logical_path_map[logical_path].union(content_files)
    
    return logical_path_map