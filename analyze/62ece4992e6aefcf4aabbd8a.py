def load_configurations(config_filenames, overrides=None, resolve_env=True):
    """
    कॉनफिगरेशन फाइलों के अनुक्रम को दिया गया है, प्रत्येक कॉनफिगरेशन फाइल को लोड और सत्यापित करें।
    परिणाम को निम्नलिखित के रूप में ट्यूपल में लौटाएं:
    1. कॉनफिगरेशन फाइल नाम और उसके संबंधित पार्स किए गए कॉनफिगरेशन का डिक्शनरी।
    2. किसी भी पार्स त्रुटियों को शामिल करने वाले `logging.LogRecord` इंस्टेंस का अनुक्रम।
    """
    import yaml
    import os
    import logging
    from collections import OrderedDict

    # Initialize return values
    configs = OrderedDict()
    log_records = []
    logger = logging.getLogger(__name__)

    # Process each config file
    for filename in config_filenames:
        try:
            with open(filename, 'r') as f:
                config = yaml.safe_load(f)
                
                # Resolve environment variables if requested
                if resolve_env:
                    config = _resolve_env_vars(config)
                
                # Apply any overrides
                if overrides:
                    config = _apply_overrides(config, overrides)
                
                configs[filename] = config
                
        except (yaml.YAMLError, IOError) as e:
            # Create log record for error
            record = logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=filename,
                lineno=0,
                msg=str(e),
                args=(),
                exc_info=None
            )
            log_records.append(record)
            logger.error(f"Error loading config file {filename}: {str(e)}")
            
    return configs, log_records

def _resolve_env_vars(config):
    """Helper function to resolve environment variables in config"""
    if isinstance(config, dict):
        return {k: _resolve_env_vars(v) for k, v in config.items()}
    elif isinstance(config, list):
        return [_resolve_env_vars(v) for v in config]
    elif isinstance(config, str):
        # Replace ${VAR} or $VAR with environment variable
        if config.startswith('$'):
            var = config.lstrip('${').rstrip('}')
            return os.environ.get(var, config)
    return config

def _apply_overrides(config, overrides):
    """Helper function to apply override values to config"""
    if isinstance(config, dict):
        config = config.copy()
        for k, v in overrides.items():
            if k in config and isinstance(config[k], dict) and isinstance(v, dict):
                config[k] = _apply_overrides(config[k], v)
            else:
                config[k] = v
    return config