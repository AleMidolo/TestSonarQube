def simulate_operation(self):
    """
        थर्मोस्टेट के संचालन का अनुकरण करें। यह स्वचालित रूप से संचालन मोड सेट करने के लिए auto_set_mode विधि शुरू करेगा,
        और फिर लक्षित तापमान तक पहुँचने तक संचालन मोड के अनुसार वर्तमान तापमान को स्वचालित रूप से समायोजित करेगा।
        :return time: int, अनुकरण पूरा करने में लगा समय।
        >>> thermostat = Thermostat(20.4, 37.5, 'cool')
        >>> thermostat.simulate_operation()
        18
        """
    self.auto_set_mode()
    time_taken = 0
    while abs(self.current_temperature - self.target_temperature) > 0.1:
        if self.mode == 'heat':
            self.current_temperature += 1.0
        else:
            self.current_temperature -= 1.0
        time_taken += 1
        time.sleep(0.01)
    return time_taken