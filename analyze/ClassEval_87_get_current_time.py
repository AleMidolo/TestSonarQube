from datetime import datetime

def get_current_time(self):
    """
    वर्तमान समय को '%H:%M:%S' के प्रारूप में लौटाएं
    :return: स्ट्रिंग
    >>> timeutils = TimeUtils()
    >>> timeutils.get_current_time()
    "19:19:22"
    """
    return datetime.now().strftime('%H:%M:%S')