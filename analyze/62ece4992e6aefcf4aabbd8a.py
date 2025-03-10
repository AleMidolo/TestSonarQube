import logging
import json
import yaml
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
                if filename.endswith('.json'):
                    config = json.load(file)
                elif filename.endswith('.yaml') or filename.endswith('.yml'):
                    config = yaml.safe_load(file)
                else:
                    logging.error(f"Unsupported file format: {filename}")
                    errors.append(logging.LogRecord(
                        name=__name__,
                        level=logging.ERROR,
                        pathname=__file__,
                        lineno=0,
                        msg=f"Unsupported file format: {filename}",
                        args=None,
                        exc_info=None
                    ))
                    continue

                if resolve_env:
                    for key, value in config.items():
                        if isinstance(value, str) and value.startswith('$'):
                            env_var = value[1:]
                            config[key] = os.getenv(env_var, value)

                if overrides:
                    for key, value in overrides.items():
                        config[key] = value

                configurations[filename] = config

        except Exception as e:
            logging.error(f"Error loading configuration file {filename}: {e}")
            errors.append(logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=__file__,
                lineno=0,
                msg=f"Error loading configuration file {filename}: {e}",
                args=None,
                exc_info=None
            ))

    return configurations, errors