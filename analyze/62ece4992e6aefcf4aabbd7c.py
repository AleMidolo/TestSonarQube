def oneline(script, separator=" && "):
    """
    एक स्क्रिप्ट को एक लाइन कमांड में बदलता है।
    यह एकल SSH कमांड चलाने और एक लाइन स्क्रिप्ट पास करने के लिए उपयोगी है।

    :param script: str, स्क्रिप्ट जिसे एक लाइन में बदलना है।
    :param separator: str, विभाजक जो कमांड्स के बीच उपयोग किया जाएगा। डिफ़ॉल्ट रूप से " && "।
    :return: str, एक लाइन में परिवर्तित स्क्रिप्ट।
    """
    lines = script.strip().splitlines()
    return separator.join(line.strip() for line in lines if line.strip())