def formatmany(
        self,
        sql: AnyStr,
        many_params: Union[Iterable[Dict[Union[str, int], Any]], Iterable[Sequence[Any]]],
) -> Tuple[AnyStr, Union[List[Dict[Union[str, int], Any]], List[Sequence[Any]]]]:
    """
    यह फ़ंक्शन SQL क्वेरी को "in-style" पैरामीटर्स से "out-style" पैरामीटर्स में बदलने के लिए उपयोग किया जाता है।

    - *`sql`* (`str` या `bytes`): यह SQL क्वेरी है जिसे कन्वर्ट करना है।
    
    - *`many_params`* (`~collections.abc.Iterable`): यह "in-style" पैरामीटर्स के सेट को रखता है।  
      - *`params`* (`~collections.abc.Mapping` या `~collections.abc.Sequence`):  
        यह "in-style" पैरामीटर्स का सेट है। यह प्रत्येक पैरामीटर (`str` या `int`) को उसके मान (value) से मैप करता है।  
        - यदि `SQLParams.in_style` एक नामित पैरामीटर स्टाइल है, तो `params` को `~collections.abc.Mapping` होना चाहिए।  
        - यदि `SQLParams.in_style` एक ऑर्डिनल पैरामीटर स्टाइल है, तो `params` को `~collections.abc.Sequence` होना चाहिए।
    रिटर्न:
    यह फ़ंक्शन एक `tuple` रिटर्न करता है जिसमें शामिल हैं:
    1. *फ़ॉर्मेट की गई SQL क्वेरी* (`str` या `bytes`)।
    2. *कन्वर्ट किए गए "out-style" पैरामीटर्स का सेट* (`list`), जो `dict` या `list` के रूप में होता है।
    """
    formatted_sql = sql
    out_params = []

    for params in many_params:
        if isinstance(params, dict):
            # Handle named parameters
            out_params.append({k: v for k, v in params.items()})
        elif isinstance(params, (list, tuple)):
            # Handle ordinal parameters
            out_params.append([v for v in params])
        else:
            raise TypeError("Unsupported parameter type. Expected dict or sequence.")

    return formatted_sql, out_params