def get_logical_path_map(inventory, version):
    """
    इन्वेंटरी में दिए गए संस्करण (version) के लिए स्थिति (state) में लॉजिकल पथों और डिस्क पर फ़ाइलों के बीच का मैप प्राप्त करें।

    रिटर्न करता है एक डिक्शनरी: 
    `logical_path_in_state -> set(content_files)`

    `content_files` का सेट उन डुप्लिकेट फ़ाइलों के संदर्भ भी शामिल कर सकता है जो उस संस्करण के बाद के संस्करणों में मौजूद हैं जिसे वर्णित किया जा रहा है।
    """
    logical_path_map = {}
    
    for logical_path, file_versions in inventory.items():
        content_files = set()
        for file_version, files in file_versions.items():
            if file_version <= version:
                content_files.update(files)
        if content_files:
            logical_path_map[logical_path] = content_files
    
    return logical_path_map