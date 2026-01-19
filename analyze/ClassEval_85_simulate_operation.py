def simulate_operation(self):
    """
    थर्मोस्टेट के संचालन का अनुकरण करें। यह स्वचालित रूप से संचालन मोड सेट करने के लिए auto_set_mode विधि शुरू करेगा,
    और फिर लक्षित तापमान तक पहुँचने तक संचालन मोड के अनुसार वर्तमान तापमान को स्वचालित रूप से समायोजित करेगा।
    :return time: int, अनुकरण पूरा करने में लगा समय।
    >>> thermostat = Thermostat(20.4, 37.5, 'cool')
    >>> thermostat.simulate_operation()
    18
    """
    # First, automatically set the mode based on current and target temperature
    self.auto_set_mode()
    
    time = 0
    
    # Continue adjusting temperature until target is reached
    while self.current_temp != self.target_temp:
        if self.mode == 'heat':
            # Heating mode: increase temperature
            self.current_temp += 1
        elif self.mode == 'cool':
            # Cooling mode: decrease temperature
            self.current_temp -= 1
        # If mode is 'off', temperature doesn't change
        
        time += 1
    
    return time