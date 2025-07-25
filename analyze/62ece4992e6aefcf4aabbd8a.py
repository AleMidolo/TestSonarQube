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
    errors = []

    for filename in config_filenames:
        try:
            with open(filename, 'r') as file:
                config_data = json.load(file)
                
                if resolve_env:
                    for key, value in config_data.items():
                        if isinstance(value, str) and value.startswith('$'):
                            env_var = value[1:]
                            config_data[key] = os.getenv(env_var, value)
                
                if overrides:
                    config_data.update(overrides)
                
                configurations[filename] = config_data
        except json.JSONDecodeError as e:
            error_msg = f"JSON पार्स त्रुटि: {filename} - {str(e)}"
            logging.error(error_msg)
            errors.append(logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=__file__,
                lineno=e.lineno,
                msg=error_msg,
                args=None,
                exc_info=None
            ))
        except Exception as e:
            error_msg = f"त्रुटि: {filename} - {str(e)}"
            logging.error(error_msg)
            errors.append(logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=__file__,
                lineno=0,
                msg=error_msg,
                args=None,
                exc_info=None
            ))

    return configurations, errors