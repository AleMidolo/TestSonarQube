def oneline(script, seperator=" && "):
    """
    Converts a script to one line command.
    This is useful to run a single ssh command and pass a one line script.

    :param script: A list of commands or a multi-line string of commands.
    :param seperator: The separator used to join the commands (default is " && ").
    :return: A single-line string of commands.
    """
    if isinstance(script, str):
        # Split the multi-line string into individual commands
        commands = [cmd.strip() for cmd in script.splitlines() if cmd.strip()]
    else:
        # Assume it's a list of commands
        commands = [cmd.strip() for cmd in script if cmd.strip()]
    
    # Join the commands with the specified separator
    return seperator.join(commands)