import logging

def build_app_logger(name='app', logfile='app.log', debug=True):
    """
    सामान्य उद्देश्य के लिए एप्लिकेशन लॉगर। मुख्य रूप से डिबगिंग के लिए उपयोगी।
    
    Args:
        name (str): लॉगर का नाम। डिफ़ॉल्ट 'app' है।
        logfile (str): लॉग फ़ाइल का नाम। डिफ़ॉल्ट 'app.log' है।
        debug (bool): यदि True है, तो डिबग स्तर पर लॉगिंग करें। अन्यथा, INFO स्तर पर लॉगिंग करें।
    
    Returns:
        logging.Logger: कॉन्फ़िगर किया गया लॉगर।
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    
    # फ़ाइल में लॉग करने के लिए हैंडलर
    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.DEBUG if debug else logging.INFO)
    
    # कंसोल पर लॉग करने के लिए हैंडलर
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if debug else logging.INFO)
    
    # लॉग फ़ॉर्मेट
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # हैंडलर को लॉगर में जोड़ें
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger