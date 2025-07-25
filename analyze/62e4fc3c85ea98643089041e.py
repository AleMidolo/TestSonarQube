def _inline_r_setup(code: str) -> str:
    # Set up R options that can only be configured after R starts
    setup_code = """
    options(warn=-1)  # Suppress warnings
    options(width=120)  # Set output width
    options(scipen=10)  # Reduce scientific notation
    options(digits.secs=3)  # Display milliseconds in times
    """
    
    # Combine setup code with user code
    full_code = setup_code + "\n" + code
    
    return full_code