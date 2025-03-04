def _create_converter(self) -> _converting._Converter:
    """
    पैरामीटर स्टाइल कन्वर्टर बनाएं।

    रिटर्न करता है पैरामीटर स्टाइल कन्वर्टर (:class:`._converting._Converter`)।
    """
    return _converting._Converter(
        self._style_name,
        self._style_config,
        self._style_mapping
    )