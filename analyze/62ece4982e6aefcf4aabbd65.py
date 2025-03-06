def parser_flags(parser):
    """
    एक argparse.ArgumentParser उदाहरण के लिए, इसके आर्गुमेंट फ्लैग्स को एक स्पेस से अलग किए गए स्ट्रिंग के रूप में लौटाएं।
    """
    flags = []
    for action in parser._actions:
        if action.option_strings:
            flags.extend(action.option_strings)
    return ' '.join(flags)