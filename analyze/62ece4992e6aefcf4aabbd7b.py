import os

def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    एक लक्षित कॉन्फ़िग फ़ाइल नाम और रेंडर किया गया YAML कॉन्फ़िग दिए जाने पर, इसे फ़ाइल में लिखें। 
    आवश्यकतानुसार किसी भी समाहित डायरेक्टरी को बनाएं। 
    लेकिन यदि फ़ाइल पहले से मौजूद है और `overwrite` False है, तो कुछ भी लिखने से पहले प्रक्रिया को रोक दें।
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(config_filename), exist_ok=True)
    
    # Check if the file exists and overwrite is False
    if not overwrite and os.path.exists(config_filename):
        raise FileExistsError(f"{config_filename} already exists and overwrite is set to False.")
    
    # Write the rendered configuration to the file
    with open(config_filename, 'w') as config_file:
        config_file.write(rendered_config)
    
    # Set the file permissions
    os.chmod(config_filename, mode)