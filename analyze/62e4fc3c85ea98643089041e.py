def _inline_r_setup(code: str) -> str:
    r_setup = """
    options(warn=-1)
    options(width=120)
    """
    
    # Combine setup code with input code
    full_code = r_setup + "\n" + code
    
    return full_code