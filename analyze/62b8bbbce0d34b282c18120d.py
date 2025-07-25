def is_file_exist(file_name):
    """
    फ़ाइल नाम की जाँच करें कि वह मौजूद है या नहीं।  
    :param file_name: फ़ाइल का नाम।  
    :type file_name: str  
    :return: true लौटाएगा (यदि फ़ाइल मौजूद है), false लौटाएगा (यदि फ़ाइल मौजूद नहीं है या फ़ाइल नाम अमान्य है)।  
    :rtype: bool  
    """
    import os
    
    try:
        return os.path.exists(file_name)
    except:
        return False