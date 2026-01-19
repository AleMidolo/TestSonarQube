def add_seconds(self, seconds):
    """
    वर्तमान समय में निर्दिष्ट संख्या के सेकंड जोड़ें
    :param seconds: int, जोड़ने के लिए सेकंड की संख्या
    :return: string, निर्दिष्ट संख्या के सेकंड जोड़ने के बाद का समय '%H:%M:%S' प्रारूप में
    >>> timeutils.add_seconds(600)
    "19:29:22"
    """
    from datetime import datetime, timedelta
    
    current_time = datetime.now()
    new_time = current_time + timedelta(seconds=seconds)
    return new_time.strftime('%H:%M:%S')