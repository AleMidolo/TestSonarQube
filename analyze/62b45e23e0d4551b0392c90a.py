import os
import hashlib

def validate_version_inventories(self, version_dirs):
    """
    प्रत्येक संस्करण के पास उस बिंदु तक एक इन्वेंटरी होनी चाहिए।

    साथ ही, किसी भी सामग्री डाइजेस्ट का रिकॉर्ड रखें जो रूट इन्वेंटरी में मौजूद डाइजेस्ट से अलग हो,
    ताकि सामग्री को सत्यापित करते समय हम उन्हें भी जांच सकें।

    version_dirs एक संस्करण डायरेक्टरी नामों की सूची है और इसे संस्करण अनुक्रम (1, 2, 3...) में माना जाता है।
    """
    inventory_digests = {}
    discrepancies = []

    for version_dir in version_dirs:
        inventory_path = os.path.join(version_dir, "inventory.txt")
        if not os.path.exists(inventory_path):
            raise FileNotFoundError(f"Inventory file not found in {version_dir}")

        with open(inventory_path, 'rb') as f:
            content = f.read()
            digest = hashlib.sha256(content).hexdigest()

        if version_dir == version_dirs[0]:
            root_digest = digest
        else:
            if digest != root_digest:
                discrepancies.append((version_dir, digest))

        inventory_digests[version_dir] = digest

    return inventory_digests, discrepancies