def format(
                self,
                sql: AnyStr,
                params: Union[Dict[Union[str, int], Any], Sequence[Any]],
        ) -> Tuple[AnyStr, Union[Dict[Union[str, int], Any], Sequence[Any]]]:
    """
    SQL क्वेरी को "in-style" पैरामीटर्स के बजाय "out-style" पैरामीटर्स का उपयोग करने के लिए कन्वर्ट करें।

    *sql* (:class:`str` या :class:`bytes`) SQL क्वेरी है।

    *params* (:class:`~collections.abc.Mapping` या :class:`~collections.abc.Sequence`)  
    "in-style" पैरामीटर्स का सेट है। यह प्रत्येक पैरामीटर (:class:`str` या :class:`int`) को उसके मान से मैप करता है।  
    यदि :attr:`.SQLParams.in_style` एक नामित पैरामीटर शैली है, तो *params* को :class:`~collections.abc.Mapping` होना चाहिए।  
    यदि :attr:`.SQLParams.in_style` एक क्रमबद्ध पैरामीटर शैली है, तो *params* को :class:`~collections.abc.Sequence` होना चाहिए।

    यह एक :class:`tuple` लौटाता है जिसमें शामिल हैं:

    -       फॉर्मेट की गई SQL क्वेरी (:class:`str` या :class:`bytes`)।

    -       कन्वर्ट किए गए "out-style" पैरामीटर्स का सेट (:class:`dict` या :class:`list`)।
    """
    if isinstance(params, dict):
        # Named parameters
        for key, value in params.items():
            sql = sql.replace(f":{key}", str(value))
        return sql, list(params.values())
    elif isinstance(params, (list, tuple)):
        # Positional parameters
        for index, value in enumerate(params):
            sql = sql.replace(f"?{index}", str(value))
        return sql, params
    else:
        raise TypeError("params must be a dictionary or a sequence")