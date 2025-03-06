def inject_config(self):
    """
    कॉन्फ़िग पथ के लिए पर्यावरण वेरिएबल सेट करें, यदि यह परिभाषित नहीं है।
    """
    import os
    config_path = os.getenv('CONFIG_PATH')
    if not config_path:
        os.environ['CONFIG_PATH'] = '/path/to/default/config'