def list_of_file_names(settings_dirs, spec_option):
    """
    एक नया IniType कॉम्प्लेक्स टाइप बनाएं

    :param settings_dirs: सेटिंग्स डायरेक्टरीज़ की सूची
    :param spec_option: विशेष विकल्प
    :return: फ़ाइल नामों की सूची
    """
    import os
    file_names = []
    for directory in settings_dirs:
        if os.path.isdir(directory):
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if spec_option in file:
                        file_names.append(os.path.join(root, file))
    return file_names