def _create_converter(self) -> _converting._Converter:
    """
    पैरामीटर स्टाइल कन्वर्टर बनाएं।

    रिटर्न करता है पैरामीटर स्टाइल कन्वर्टर (:class:`._converting._Converter`)।
    """
    return _converting._Converter(
        style=self._style,
        case=self._case,
        separator=self._separator
    )