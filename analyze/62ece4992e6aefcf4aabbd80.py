def remove_ending_os_sep(input_list):
    """
    विवरण:
    एक स्ट्रिंग सूची पर पुनरावृत्ति करें और अंतिम OS विभाजक वर्णों को हटा दें।  
    प्रत्येक स्ट्रिंग की जांच की जाती है कि उसकी लंबाई एक से अधिक है और क्या उसका अंतिम वर्ण पथनाम विभाजक है।  
    यदि ऐसा है, तो पथनाम विभाजक वर्ण को हटा दिया जाता है।  

    तर्क (Arguments):
    - `input_list`: स्ट्रिंग्स की सूची।  

    रिटर्न (Returns):
    - प्रोसेस की गई स्ट्रिंग्स की सूची।  

    त्रुटि (Raises):
    - `TypeError`: यदि इनपुट सूची का प्रकार सही नहीं है।  
    """
    import os
    
    # Check input type
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
        
    result = []
    for item in input_list:
        # Check if item is string
        if not isinstance(item, str):
            raise TypeError("All list items must be strings")
            
        # Check if string length > 1 and ends with path separator
        if len(item) > 1 and item.endswith(os.sep):
            result.append(item[:-1])
        else:
            result.append(item)
            
    return result