def bash_completion():
    import borgmatic
    import argparse

    parser = borgmatic.create_parser()
    completion_script = parser.format_help()
    
    return completion_script