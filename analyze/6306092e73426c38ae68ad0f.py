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
        key = arg.split('=')[0].strip('--')  # Remove -- prefix
        value = arg.split('=')[1] if '=' in arg else True
        
        # Convert string values to appropriate types
        if isinstance(value, str):
            if value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False
            elif value.isdigit():
                value = int(value)
            elif value.replace('.','',1).isdigit():
                value = float(value)
                
        # Categorize arguments
        if key in control_arg_list:
            control_args[key] = value
        elif key.startswith('custom_'):
            custom_args[key] = value
        else:
            # Handle nested arguments with dot notation
            if '.' in key:
                parts = key.split('.')
                current = nested_args
                for part in parts[:-1]:
                    if part not in current:
                        current[part] = {}
                    current = current[part]
                current[parts[-1]] = value
            else:
                nested_args[key] = value
                
    # Merge custom args into nested args
    if custom_args:
        nested_args['custom'] = custom_args
        
    return control_args, nested_args