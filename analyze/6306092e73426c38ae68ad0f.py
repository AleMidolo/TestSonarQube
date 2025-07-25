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
    custom_args = {}

    # Control arguments that should not be included in spec.yml
    control_arg_list = ['debug', 'verbose', 'dry_run', 'no_color']
    
    # Process each argument
    for arg in args:
        key = arg.split('=')[0] if '=' in arg else arg
        value = arg.split('=')[1] if '=' in arg else None
        
        # Remove leading dashes from key
        key = key.lstrip('-')
        
        # Handle control arguments
        if key in control_arg_list:
            control_args[key] = value if value is not None else True
            continue
            
        # Handle custom arguments (starting with 'custom_')
        if key.startswith('custom_'):
            custom_args[key] = value
            continue
            
        # Handle nested arguments
        parts = key.split('.')
        current_dict = nested_args
        
        # Build nested structure
        for part in parts[:-1]:
            if part not in current_dict:
                current_dict[part] = {}
            current_dict = current_dict[part]
            
        # Set the final value
        current_dict[parts[-1]] = value if value is not None else True

    # Merge custom args into nested args
    if custom_args:
        nested_args['custom'] = custom_args

    return control_args, nested_args