def _inline_r_setup(code: str) -> str:
    # R options that need to be set after startup
    r_setup = """
    options(warn=-1)  # Suppress warnings
    options(width=120)  # Set output width
    options(scipen=999)  # Disable scientific notation
    """
    
    # Combine setup code with input code
    full_code = r_setup + "\n" + code
    
    return full_code