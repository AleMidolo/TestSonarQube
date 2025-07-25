def parser_flags(parser):
    """
    दिए गए argparse.ArgumentParser इंस्टेंस के लिए, इसके आर्गुमेंट फ्लैग्स को एक स्पेस-सेपरेटेड 
    स्ट्रिंग के रूप में रिटर्न करें।
    """
    flags = []
    for action in parser._actions:
        # Skip help action
        if action.dest == 'help':
            continue
            
        # Get all option strings (flags) for this argument
        for opt in action.option_strings:
            flags.append(opt)
            
    # Return space-separated string of flags
    return ' '.join(sorted(flags))