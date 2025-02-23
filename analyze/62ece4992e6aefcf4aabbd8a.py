import logging
import json
import os

def load_configurations(config_filenames, overrides=None, resolve_env=True):
    """
    कॉनफिगरेशन फाइलों के अनुक्रम को दिया गया है, प्रत्येक कॉनफिगरेशन फाइल को लोड और सत्यापित करें। 
    परिणाम को निम्नलिखित के रूप में ट्यूपल में लौटाएं:
    1. कॉनफिगरेशन फाइल नाम और उसके संबंधित पार्स किए गए कॉनफिगरेशन का डिक्शनरी।
    2. किसी भी पार्स त्रुटियों को शामिल करने वाले `logging.LogRecord` इंस्टेंस का अनुक्रम।
    """
    configurations = {}
    log_records = []
    
    for filename in config_filenames:
        try:
            with open(filename, 'r') as file:
                config = json.load(file)
                
                if resolve_env:
                    for key, value in config.items():
                        if isinstance(value, str) and value.startswith('$'):
                            env_var = value[1:]
                            config[key] = os.getenv(env_var, value)
                
                if overrides:
                    config.update(overrides)
                
                configurations[filename] = config
                
        except Exception as e:
            log_record = logging.LogRecord(
                name='config_loader',
                level=logging.ERROR,
                pathname=filename,
                lineno=0,
                msg=str(e),
                args=None,
                exc_info=True
            )
            log_records.append(log_record)
    
    return configurations, log_records