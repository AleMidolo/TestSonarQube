def _inline_r_setup(code: str) -> str:
    # Define R setup options that need to be prepended to the code
    r_setup = """
options(warn=-1)  # Suppress warnings
options(width=10000)  # Prevent line wrapping
options(digits.secs=3)  # Show milliseconds in times
options(scipen=999)  # Prevent scientific notation
"""
    
    # Combine the setup code with the input code
    return r_setup + "\n" + code