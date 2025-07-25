def get_spec_defaults(self):
    """
    Risolvere i valori degli argomenti dal file di specifica e da altre fonti.
    """
    # Assuming the specification file is a JSON file named 'spec.json'
    import json
    import os

    # Load the specification file
    spec_file_path = 'spec.json'
    if os.path.exists(spec_file_path):
        with open(spec_file_path, 'r') as file:
            spec_data = json.load(file)
    else:
        spec_data = {}

    # Here you can add logic to resolve values from other sources if needed
    # For example, environment variables, command-line arguments, etc.

    # Return the resolved values
    return spec_data