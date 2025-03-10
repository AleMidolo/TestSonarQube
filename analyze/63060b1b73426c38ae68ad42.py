def inject_config(self):
    """
    कॉन्फ़िग पथ के लिए पर्यावरण वेरिएबल सेट करें, यदि यह परिभाषित नहीं है।
    """
    import os
    if 'CONFIG_PATH' not in os.environ:
        os.environ['CONFIG_PATH'] = '/path/to/default/config'