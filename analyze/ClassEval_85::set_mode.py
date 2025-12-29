def set_mode(self, mode):
    """
        वर्तमान कार्य मोड प्राप्त करें
        :param mode: str, कार्य मोड. केवल ['heat', 'cool']
        >>> thermostat.set_mode('cool')
        >>> thermostat.mode
        'cool'
        """
    if mode in ['heat', 'cool']:
        self.mode = mode
    else:
        raise ValueError("Mode must be either 'heat' or 'cool'")