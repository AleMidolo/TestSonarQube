def auto_check_conflict(self):
    """
    जांचें कि क्या संचालन मोड और वर्तमान तापमान और लक्षित तापमान के बीच संबंध में कोई संघर्ष है।
    यदि कोई संघर्ष है, तो संचालन मोड को स्वचालित रूप से समायोजित किया जाएगा।
    :return: यदि मोड वर्तमान तापमान और लक्षित तापमान के बीच संबंध के साथ संघर्ष नहीं करता है, तो True, अन्यथा False।
    >>> thermostat = Thermostat(20.4, 37.5, 'cool')
    >>> thermostat.auto_check_conflict()
    False
    >>> thermostat.mode
    'heat'
    """
    if self.mode == 'heat' and self.current_temperature >= self.target_temperature or (self.mode == 'cool' and self.current_temperature <= self.target_temperature):
        self.auto_set_mode()
        return False
    return True