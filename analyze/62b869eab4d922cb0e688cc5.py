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
    """
    for field, value in observer_schema.items():
        if isinstance(value, dict):
            # Handle nested dictionary
            if field not in last_applied_manifest:
                last_applied_manifest[field] = {}
            if field not in response:
                raise KeyError(f"Field {field} not found in Kubernetes response")
            update_last_applied_manifest_dict_from_resp(
                last_applied_manifest[field], value, response[field]
            )
        elif isinstance(value, list):
            # Handle list fields
            if field not in last_applied_manifest:
                if field not in response:
                    raise KeyError(f"Field {field} not found in Kubernetes response")
                last_applied_manifest[field] = response[field]
        else:
            # Handle primitive fields
            if field not in last_applied_manifest:
                if field not in response:
                    raise KeyError(f"Field {field} not found in Kubernetes response")
                last_applied_manifest[field] = response[field]

    return last_applied_manifest