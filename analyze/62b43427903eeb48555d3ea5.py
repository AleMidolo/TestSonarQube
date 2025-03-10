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
        # Convert named parameters to out-style
        out_params = {}
        for key, value in params.items():
            out_params[f":{key}"] = value
        formatted_sql = sql
        for key, value in params.items():
            formatted_sql = formatted_sql.replace(f":{key}", "?")
        return formatted_sql, list(out_params.values())
    elif isinstance(params, (list, tuple)):
        # Convert positional parameters to out-style
        formatted_sql = sql
        for i in range(len(params)):
            formatted_sql = formatted_sql.replace(f"?", "?", 1)
        return formatted_sql, list(params)
    else:
        raise TypeError("params must be a dict, list, or tuple")