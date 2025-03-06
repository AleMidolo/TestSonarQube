def initialize(self):
    """
    एक नया OCFL स्टोरेज रूट बनाएँ और प्रारंभ करें।
    """
    import os
    import json

    # OCFL रूट डायरेक्टरी बनाएँ
    if not os.path.exists('ocfl_root'):
        os.makedirs('ocfl_root')

    # OCFL संस्करण फ़ाइल बनाएँ
    ocfl_version = {
        "type": "https://ocfl.io/1.0/spec/#inventory",
        "digestAlgorithm": "sha512",
        "head": None,
        "versions": {}
    }

    with open(os.path.join('ocfl_root', 'ocfl_1.0.json'), 'w') as f:
        json.dump(ocfl_version, f, indent=4)

    # OCFL नामस्थान फ़ाइल बनाएँ
    with open(os.path.join('ocfl_root', '0=ocfl_1.0'), 'w') as f:
        f.write("ocfl_1.0\n")

    # OCFL रूट में एक नामस्थान फ़ाइल बनाएँ
    with open(os.path.join('ocfl_root', '0=ocfl_object_1.0'), 'w') as f:
        f.write("ocfl_object_1.0\n")

    print("OCFL स्टोरेज रूट सफलतापूर्वक प्रारंभ किया गया।")