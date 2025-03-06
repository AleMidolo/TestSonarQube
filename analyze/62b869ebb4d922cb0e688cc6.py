def update_last_applied_manifest_list_from_resp(
    last_applied_manifest, observer_schema, response
):
    """
    साथ में :func:``update_last_applied_manifest_dict_from_resp``, यह फ़ंक्शन 
    पुनरावृत्त रूप से कॉल किया जाता है ताकि आंशिक ``last_applied_manifest`` को 
    आंशिक Kubernetes प्रतिक्रिया से अपडेट किया जा सके।

    आर्ग्युमेंट्स (Args):
        last_applied_manifest (list): आंशिक ``last_applied_manifest`` जो 
            अपडेट किया जा रहा है।
        observer_schema (list): आंशिक ``observer_schema``।
        response (list): Kubernetes API से प्राप्त आंशिक प्रतिक्रिया।

    यह फ़ंक्शन सभी देखे गए फ़ील्ड्स (observed fields) के माध्यम से जाता है और 
    यदि वे पहले से मौजूद नहीं हैं तो उनके मान को ``last_applied_manifest`` में 
    आरंभ (initialize) करता है।
    """
    for i, (schema_item, resp_item) in enumerate(zip(observer_schema, response)):
        if isinstance(schema_item, dict) and isinstance(resp_item, dict):
            update_last_applied_manifest_dict_from_resp(
                last_applied_manifest[i], schema_item, resp_item
            )
        elif isinstance(schema_item, list) and isinstance(resp_item, list):
            update_last_applied_manifest_list_from_resp(
                last_applied_manifest[i], schema_item, resp_item
            )
        else:
            if i >= len(last_applied_manifest):
                last_applied_manifest.append(resp_item)
            else:
                last_applied_manifest[i] = resp_item