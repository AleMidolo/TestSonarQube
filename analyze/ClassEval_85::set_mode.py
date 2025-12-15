def set_mode(self, mode):
        """
        वर्तमान कार्य मोड प्राप्त करें
        :param mode: str, कार्य मोड. केवल ['heat', 'cool']
        >>> thermostat.set_mode('cool')
        >>> thermostat.mode
        'cool'
        """
        self.mode = mode