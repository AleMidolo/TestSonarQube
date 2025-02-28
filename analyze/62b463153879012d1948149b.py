import os

def match_file_by_prefix(prefix, file_path):
    """
    पहचानें कि क्या `file_path` किसी दिए गए `prefix` द्वारा दस्तावेज़ पैकेज से संबंधित है

    एक पैकेज से संबंधित दस्तावेज़ों के लिए `True` लौटाएँ।

    पैरामीटर
    ----------
    prefix : str
        फ़ाइलनाम उपसर्ग
    file_path : str
        फ़ाइल पथ
    रिटर्न
    -------
    bool
        सत्य - फ़ाइल पैकेज से संबंधित है
    """
    # Get the filename from the file path
    filename = os.path.basename(file_path)
    
    # Check if the filename starts with the given prefix
    return filename.startswith(prefix)