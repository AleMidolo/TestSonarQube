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
    control_arg_keys = ['debug', 'verbose', 'dry_run', 'no_color']
    
    # Process each argument
    for arg in args:
        key = arg.get('name')
        value = arg.get('value')
        
        # Check if argument is a control argument
        if key in control_arg_keys:
            control_args[key] = value
            continue
            
        # Check if argument is a custom argument (starts with 'custom_')
        if key.startswith('custom_'):
            custom_args[key] = value
            continue
            
        # All other arguments are treated as nested
        nested_path = key.split('.')
        current_dict = nested_args
        
        # Build nested dictionary structure
        for i, path_part in enumerate(nested_path):
            if i == len(nested_path) - 1:
                current_dict[path_part] = value
            else:
                if path_part not in current_dict:
                    current_dict[path_part] = {}
                current_dict = current_dict[path_part]

    # Merge custom args into nested args
    nested_args.update(custom_args)
    
    return control_args, nested_args