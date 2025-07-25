def update_last_applied_manifest_dict_from_resp(
    last_applied_manifest, observer_schema, response
):
    """
    :func:``update_last_applied_manifest_list_from_resp`` के साथ मिलकर, यह फ़ंक्शन आंशिक ``last_applied_manifest`` को आंशिक Kubernetes प्रतिक्रिया से अपडेट करने के लिए पुनरावृत्त रूप से कॉल किया जाता है।

    आर्ग्युमेंट्स (Args):
        last_applied_manifest (dict): आंशिक ``last_applied_manifest`` जिसे अपडेट किया जा रहा है।
        observer_schema (dict): आंशिक ``observer_schema``।
        response (dict): Kubernetes API से प्राप्त आंशिक प्रतिक्रिया।

    त्रुटि (Raises):
        KeyError: यदि देखे गए फ़ील्ड Kubernetes प्रतिक्रिया में मौजूद नहीं हैं।

    यह फ़ंक्शन सभी देखे गए फ़ील्ड्स के माध्यम से जाता है और यदि वे पहले से ``last_applied_manifest`` में मौजूद नहीं हैं, तो उनके मान को इनिशियलाइज़ करता है।
    """
    for key in observer_schema:
        if key not in last_applied_manifest:
            if key not in response:
                raise KeyError(f"Field '{key}' not found in response.")
            last_applied_manifest[key] = response[key]
    return last_applied_manifest