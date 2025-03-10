import os
import hashlib

def validate_version_inventories(self, version_dirs):
    """
    प्रत्येक संस्करण के पास उस बिंदु तक एक इन्वेंटरी होनी चाहिए।

    साथ ही, किसी भी सामग्री डाइजेस्ट का रिकॉर्ड रखें जो रूट इन्वेंटरी में मौजूद डाइजेस्ट से अलग हो,
    ताकि सामग्री को सत्यापित करते समय हम उन्हें भी जांच सकें।

    version_dirs एक संस्करण डायरेक्टरी नामों की सूची है और इसे संस्करण अनुक्रम (1, 2, 3...) में माना जाता है।
    """
    root_inventory = {}
    discrepancies = []

    for version_dir in version_dirs:
        inventory_path = os.path.join(version_dir, "inventory.txt")
        if not os.path.exists(inventory_path):
            raise FileNotFoundError(f"Inventory not found for version: {version_dir}")

        with open(inventory_path, 'r') as file:
            current_inventory = {}
            for line in file:
                filename, filehash = line.strip().split()
                current_inventory[filename] = filehash

                if filename in root_inventory:
                    if root_inventory[filename] != filehash:
                        discrepancies.append((filename, root_inventory[filename], filehash))
                else:
                    root_inventory[filename] = filehash

    return discrepancies