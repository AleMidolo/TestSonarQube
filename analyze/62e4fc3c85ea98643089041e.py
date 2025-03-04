def _inline_r_setup(code: str) -> str:
    # Define R setup commands
    r_setup = """
    options(warn=-1)  # Suppress warnings
    options(width=1000)  # Increase output width
    options(scipen=999)  # Prevent scientific notation
    """
    
    # Combine setup with provided code
    full_code = r_setup + "\n" + code
    
    return full_code