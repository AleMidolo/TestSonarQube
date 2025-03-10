def dict_insert(dic, val, key, *keys):
    """
    एक डिक्शनरी में नेस्टेड कुंजी का मान डालें।

    नेस्टेड कुंजी के लिए मान डालने के लिए, सभी पूर्वज कुंजियों को 
    इस मेथड के आर्ग्युमेंट्स के रूप में दिया जाना चाहिए।

    उदाहरण:
      dict_insert({}, 'मान', 'कुंजी1.कुंजी2'.split('.'))

    :param dic: वह डिक्शनरी ऑब्जेक्ट जिसमें नेस्टेड कुंजी का मान डालना है।
    :param val: वह मान जो दी गई डिक्शनरी में डालना है।
    :param key: कुंजियों की श्रृंखला में पहली कुंजी जो मान को स्टोर करेगी।
    :param keys: कुंजियों की श्रृंखला में उप-कुंजियां।
    """
    if not keys:
        dic[key] = val
        return dic
    
    current = dic
    for k in keys[:-1]:
        if k not in current:
            current[k] = {}
        current = current[k]
    
    current[keys[-1]] = val
    return dic