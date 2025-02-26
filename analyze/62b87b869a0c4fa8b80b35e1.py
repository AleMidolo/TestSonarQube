def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    """
    एक :class:`.histogram` को :class:`.graph` में बदलें।

    *make_value* एक फ़ंक्शन है जो ग्राफ़ के बिंदु का मान सेट करता है।
    डिफ़ॉल्ट रूप से यह बिन की सामग्री (bin content) होती है।
    *make_value* एकल मान (बिन सामग्री) को संदर्भ (context) के बिना स्वीकार करता है।

    इस विकल्प का उपयोग ग्राफ़ की त्रुटि पट्टियाँ (error bars) बनाने के लिए किया जा सकता है।
    उदाहरण के लिए, एक ऐसे हिस्टोग्राम से त्रुटियों के साथ ग्राफ़ बनाने के लिए
    जहां बिन में *mean*, *mean_error* और एक संदर्भ के साथ नामित ट्यूपल (named tuple) हो,
    आप निम्नलिखित का उपयोग कर सकते हैं:

    >>> make_value = lambda bin_: (bin_.mean, bin_.mean_error)

    *get_coordinate* यह परिभाषित करता है कि हिस्टोग्राम बिन से बनाए गए ग्राफ़ बिंदु का
    निर्देशांक (coordinate) क्या होगा। यह "left" (डिफ़ॉल्ट), "right" और "middle" हो सकता है।

    *field_names* ग्राफ़ के फ़ील्ड नाम सेट करता है। इनकी संख्या परिणाम के आयाम (dimension)
    के समान होनी चाहिए। ऊपर दिए गए *make_value* के लिए ये होंगे
    *("x", "y_mean", "y_mean_error")*।

    *scale* ग्राफ़ का स्केल बन जाता है (डिफ़ॉल्ट रूप से अज्ञात)।
    यदि यह ``True`` है, तो यह हिस्टोग्राम का स्केल उपयोग करता है।

    *hist* में केवल संख्यात्मक बिन (numeric bins) होने चाहिए (संदर्भ के बिना)
    या *make_value* को संदर्भ हटाकर एक संख्यात्मक ग्राफ़ बनाना चाहिए।

    परिणामी ग्राफ़ लौटाएं।
    """
    import numpy as np

    if make_value is None:
        make_value = lambda bin_: bin_.content

    coordinates = []
    values = []
    errors = []

    for bin_ in hist.bins:
        if get_coordinate == "left":
            coordinate = bin_.left
        elif get_coordinate == "right":
            coordinate = bin_.right
        elif get_coordinate == "middle":
            coordinate = bin_.center
        else:
            raise ValueError("Invalid value for get_coordinate")

        value_tuple = make_value(bin_)
        coordinates.append(coordinate)
        values.append(value_tuple[0])
        if len(value_tuple) > 1:
            errors.append(value_tuple[1])
        else:
            errors.append(0)

    if scale is True:
        scale_factor = hist.scale
    else:
        scale_factor = 1

    graph = {
        field_names[0]: np.array(coordinates) * scale_factor,
        field_names[1]: np.array(values) * scale_factor,
    }

    if len(errors) > 0:
        graph[field_names[2]] = np.array(errors) * scale_factor

    return graph