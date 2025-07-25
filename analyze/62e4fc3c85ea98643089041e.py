def _inline_r_setup(code: str) -> str:
    # Add R options to disable interactive features and warnings
    setup_code = """
    options(warn=-1)  # Suppress warnings
    options(show.error.messages=FALSE)  # Suppress error messages
    options(error=function() NULL)  # Return NULL on error
    options(device='png')  # Set default graphics device
    options(width=80)  # Set output width
    """
    
    # Combine setup code with user code
    full_code = setup_code + "\n" + code
    
    return full_code