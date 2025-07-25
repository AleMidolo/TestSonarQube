def oneline(script, seperator=" && "):
    """
    Converts a script to one line command.
    This is useful to run a single ssh command and pass a one line script.

    :param script: The script to convert to a one-line command.
    :param seperator: The separator to use between commands (default is " && ").
    :return: A single-line string representing the script.
    """
    if isinstance(script, str):
        # Split the script into lines, strip whitespace, and filter out empty lines
        lines = [line.strip() for line in script.splitlines() if line.strip()]
        # Join the lines with the specified separator
        return seperator.join(lines)
    elif isinstance(script, list):
        # If the script is already a list of commands, join them directly
        return seperator.join(script)
    else:
        raise ValueError("Script must be a string or a list of strings.")