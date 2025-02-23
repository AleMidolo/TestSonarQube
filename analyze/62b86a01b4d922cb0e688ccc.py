def generate_default_observer_schema_dict(manifest_dict, first_level=False):
    """
    यह फ़ंक्शन :func:``generate_default_observer_schema_list`` के साथ मिलकर पुनरावृत्त रूप से (recursively) कॉल किया जाता है ताकि किसी Kubernetes संसाधन (resource) के एक भाग से डिफ़ॉल्ट ``observer_schema`` का हिस्सा उत्पन्न किया जा सके, जिसे क्रमशः ``manifest_dict`` या ``manifest_list`` द्वारा परिभाषित किया गया है।

    आर्ग्युमेंट्स (Args):
    - manifest_dict (dict): आंशिक Kubernetes संसाधन (Partial Kubernetes resources)।
    - first_level (bool, optional): यदि True है, तो यह इंगित करता है कि डिक्शनरी Kubernetes संसाधन के पूरे observer schema का प्रतिनिधित्व करती है।

    रिटर्न्स (Returns):
    - dict: उत्पन्न आंशिक observer_schema (Generated partial observer_schema)।

    यह फ़ंक्शन ``manifest_dict`` से एक नई डिक्शनरी बनाता है और सभी non-list और non-dict मानों को ``None`` से बदल देता है।

    यदि यह ``first_level`` डिक्शनरी है (यानी किसी संसाधन के लिए पूरा ``observer_schema``), तो पहचानने वाले फ़ील्ड्स (identifying fields) के मान ``manifest`` फ़ाइल से कॉपी किए जाते हैं।
    """
    observer_schema = {}
    
    for key, value in manifest_dict.items():
        if isinstance(value, dict):
            observer_schema[key] = generate_default_observer_schema_dict(value, False)
        elif isinstance(value, list):
            observer_schema[key] = [generate_default_observer_schema_dict(item, False) if isinstance(item, dict) else None for item in value]
        else:
            observer_schema[key] = None

    if first_level:
        # Assuming 'metadata' is an identifying field that needs to be copied
        if 'metadata' in manifest_dict:
            observer_schema['metadata'] = manifest_dict['metadata']

    return observer_schema