def get_nested_custom_and_control_args(self, args):
    """
    इनपुट आर्ग्युमेंट्स को नेस्टेड और कस्टम में विभाजित करें।

    कंट्रोल आर्ग्युमेंट्स: IR (Intermediate Representation) व्यवहार को नियंत्रित करते हैं। 
        ये आर्ग्युमेंट्स spec.yml फाइल में नहीं डाले जाएंगे।
    नेस्टेड आर्ग्युमेंट्स: Ansible प्लेबुक्स द्वारा उपयोग किए जाते हैं और 
        spec.yml फाइल में डाले जाएंगे।
    कस्टम आर्ग्युमेंट्स: सामान्य नेस्टेड उपयोग के बजाय कस्टम Ansible वेरिएबल्स का उपयोग करने के लिए।

    :param args: एकत्रित आर्ग्युमेंट्स की सूची।
    :return: (dict, dict): फ्लैट डिक्शनरीज़ (control_args, nested_args)
    """
    control_args = {}
    nested_args = {}
    
    for key, value in args.items():
        if key.startswith('_'):
            control_args[key] = value
        else:
            nested_args[key] = value
    
    return control_args, nested_args