def inject_config(self):
    """
    कॉन्फ़िग पथ के लिए पर्यावरण वेरिएबल सेट करें, यदि यह परिभाषित नहीं है।
    """
    import os
    
    # Check if config path environment variable is not set
    if 'CONFIG_PATH' not in os.environ:
        # Set default config path to current directory
        default_path = os.path.join(os.getcwd(), 'config')
        os.environ['CONFIG_PATH'] = default_path