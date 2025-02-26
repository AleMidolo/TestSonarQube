def oneline(script, seperator=" && "):
    """
    converts a script to one line command.
    This is useful to run a single ssh command and pass a one line script.

    :param script: A multi-line string script to be converted to a one-liner.
    :return: A single line string with commands separated by the specified separator.
    """
    return seperator.join(line.strip() for line in script.strip().splitlines() if line.strip())