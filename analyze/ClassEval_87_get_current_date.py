def get_current_date(self):
    """
    वर्तमान तिथि को "%Y-%m-%d" प्रारूप में लौटाएं
    :return: स्ट्रिंग
    >>> timeutils.get_current_date()
    "2023-06-14"
    """
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")