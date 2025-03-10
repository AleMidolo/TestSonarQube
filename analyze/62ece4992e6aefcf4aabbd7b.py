import os
import yaml

def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    एक लक्षित कॉन्फ़िग फ़ाइल नाम और रेंडर किया गया YAML कॉन्फ़िग दिए जाने पर, इसे फ़ाइल में लिखें। 
    आवश्यकतानुसार किसी भी समाहित डायरेक्टरी को बनाएं। 
    लेकिन यदि फ़ाइल पहले से मौजूद है और `overwrite` False है, तो कुछ भी लिखने से पहले प्रक्रिया को रोक दें।
    """
    if os.path.exists(config_filename) and not overwrite:
        return
    
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(config_filename), exist_ok=True)
    
    # Write the rendered config to the file
    with open(config_filename, 'w', encoding='utf-8') as f:
        yaml.dump(rendered_config, f, default_flow_style=False)
    
    # Set the file permissions
    os.chmod(config_filename, mode)