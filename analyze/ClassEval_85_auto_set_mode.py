def auto_set_mode(self):
    """
        वर्तमान तापमान और लक्षित तापमान की तुलना करके स्वचालित रूप से संचालन मोड सेट करें। यदि वर्तमान तापमान लक्षित तापमान से कम है, तो संचालन मोड 'heat' पर सेट किया जाता है, अन्यथा इसे 'cool' पर सेट किया जाता है।
        >>> thermostat = Thermostat(20.4, 37.5, 'cool')
        >>> thermostat.auto_set_mode()
        >>> thermostat.mode
        'heat'
        """
    if self.current_temperature < self.target_temperature:
        self.mode = 'heat'
    else:
        self.mode = 'cool'