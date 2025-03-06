def get_option_spec(self, command_name):
    """
    दिए गए विकल्प नाम के लिए विनिर्देश प्राप्त करता है।
    """
    # Assuming the option specifications are stored in a dictionary
    # where the key is the command name and the value is the specification.
    option_specs = {
        "command1": "spec1",
        "command2": "spec2",
        # Add more command specifications as needed
    }
    
    # Return the specification for the given command name
    return option_specs.get(command_name, "No specification found for the given command name.")