def initialize(self):
    """
    Create and initialize a new OCFL storage root.
    """
    import os

    # Create the OCFL storage root directory
    os.makedirs(self.root_path, exist_ok=True)

    # Create the OCFL version file
    with open(os.path.join(self.root_path, "0=ocfl_1.0"), "w") as f:
        f.write("ocfl_1.0\n")

    # Create the OCFL inventory file
    with open(os.path.join(self.root_path, "inventory.json"), "w") as f:
        f.write("""{
    "id": "urn:uuid:12345678-1234-5678-1234-567812345678",
    "type": "Object",
    "digestAlgorithm": "sha512",
    "head": "v1",
    "versions": {
        "v1": {
            "created": "2023-10-01T00:00:00Z",
            "state": {},
            "message": "Initial version"
        }
    }
}""")

    # Create the OCFL object directory
    os.makedirs(os.path.join(self.root_path, "objects"), exist_ok=True)

    # Create the OCFL extensions directory
    os.makedirs(os.path.join(self.root_path, "extensions"), exist_ok=True)