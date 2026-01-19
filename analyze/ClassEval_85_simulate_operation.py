def simulate_operation(self):
    """
    थर्मोस्टेट के संचालन का अनुकरण करें। यह स्वचालित रूप से संचालन मोड सेट करने के लिए auto_set_mode विधि शुरू करेगा,
    और फिर लक्षित तापमान तक पहुँचने तक संचालन मोड के अनुसार वर्तमान तापमान को स्वचालित रूप से समायोजित करेगा।
    :return time: int, अनुकरण पूरा करने में लगा समय।
    >>> thermostat = Thermostat(20.4, 37.5, 'cool')
    >>> thermostat.simulate_operation()
    18
    """
    # पहले auto_set_mode को कॉल करें ताकि सही मोड सेट हो जाए
    self.auto_set_mode()
    
    time = 0
    
    # जब तक वर्तमान तापमान लक्षित तापमान तक नहीं पहुँच जाता
    while self.current_temp != self.target_temp:
        if self.mode == 'heat':
            # हीटिंग मोड में तापमान बढ़ाएं
            self.current_temp += 1
        elif self.mode == 'cool':
            # कूलिंग मोड में तापमान घटाएं
            self.current_temp -= 1
        # 'off' मोड में कुछ नहीं होता
        
        time += 1
    
    return time