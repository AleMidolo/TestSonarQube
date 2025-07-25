def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
    """
    स्टोरेज रूट हाइरार्की को मान्य करें।

    रिटर्न करता है:
        num_objects - जांचे गए ऑब्जेक्ट्स की संख्या
        good_objects - जांचे गए ऑब्जेक्ट्स की संख्या जो मान्य पाए गए
    """
    num_objects = 0
    good_objects = 0

    # Assuming we have a method to get all objects in the hierarchy
    objects = self.get_all_objects()

    for obj in objects:
        num_objects += 1
        is_valid = True

        if validate_objects:
            is_valid = self.validate_object(obj)
            if not is_valid and show_warnings:
                print(f"Warning: Object {obj} is invalid.")

        if check_digests and is_valid:
            is_valid = self.check_object_digest(obj)
            if not is_valid and show_warnings:
                print(f"Warning: Object {obj} has an invalid digest.")

        if is_valid:
            good_objects += 1

    return num_objects, good_objects