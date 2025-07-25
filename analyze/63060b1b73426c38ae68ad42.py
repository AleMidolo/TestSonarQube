def inject_config(self):
    """
    कॉन्फ़िग पथ के लिए पर्यावरण वेरिएबल सेट करें, यदि यह परिभाषित नहीं है।
    """
    import os

    config_path = os.getenv('CONFIG_PATH')
    if config_path is None:
        default_path = '/etc/default/config'
        os.environ['CONFIG_PATH'] = default_path