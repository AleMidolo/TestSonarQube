def parser_flags(parser):
    """
    एक argparse.ArgumentParser उदाहरण के लिए, इसके आर्गुमेंट फ्लैग्स को एक स्पेस से अलग किए गए स्ट्रिंग के रूप में लौटाएं।
    """
    flags = []
    for action in parser._actions:
        # Skip help action
        if action.dest == 'help':
            continue
            
        # Get all option strings (flags) for this argument
        for opt in action.option_strings:
            # Only include flags that start with '-'
            if opt.startswith('-'):
                flags.append(opt)
                
    # Return space-separated string of flags
    return ' '.join(sorted(flags))