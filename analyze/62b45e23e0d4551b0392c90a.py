def validate_version_inventories(self, version_dirs):
    """
    प्रत्येक संस्करण के पास उस बिंदु तक एक इन्वेंटरी होनी चाहिए।

    साथ ही, किसी भी सामग्री डाइजेस्ट का रिकॉर्ड रखें जो रूट इन्वेंटरी में मौजूद डाइजेस्ट से अलग हो,
    ताकि सामग्री को सत्यापित करते समय हम उन्हें भी जांच सकें।

    version_dirs एक संस्करण डायरेक्टरी नामों की सूची है और इसे संस्करण अनुक्रम (1, 2, 3...) में माना जाता है।
    """
    inventory_digests = set()
    discrepancies = {}

    for version in version_dirs:
        inventory_path = f"{version}/inventory.json"
        
        try:
            with open(inventory_path, 'r') as file:
                inventory = json.load(file)
                
                # Validate the inventory for the current version
                if not self.validate_inventory(inventory):
                    raise ValueError(f"Invalid inventory in {inventory_path}")

                # Record the digests from the root inventory
                if version == version_dirs[0]:  # Assuming the first version is the root
                    inventory_digests.update(inventory.get('digests', []))
                else:
                    # Check for discrepancies
                    current_digests = set(inventory.get('digests', []))
                    different_digests = current_digests - inventory_digests
                    if different_digests:
                        discrepancies[version] = different_digests

        except FileNotFoundError:
            raise FileNotFoundError(f"Inventory file not found: {inventory_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON from {inventory_path}")

    return discrepancies