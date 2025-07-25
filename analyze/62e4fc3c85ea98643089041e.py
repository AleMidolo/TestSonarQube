def _inline_r_setup(code: str) -> str:
    # Add R options to disable interactive features and warnings
    setup_code = """
    options(warn=-1)  # Suppress warnings
    options(show.error.messages=FALSE)  # Suppress error messages
    options(echo=FALSE)  # Disable echoing of commands
    options(interactive=FALSE)  # Disable interactive mode
    """
    
    # Combine setup code with provided code
    full_code = setup_code + "\n" + code
    
    return full_code