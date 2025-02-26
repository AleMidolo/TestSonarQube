def parser_flags(parser):
    """
    एक argparse.ArgumentParser उदाहरण के लिए, इसके आर्गुमेंट फ्लैग्स को एक स्पेस से अलग किए गए स्ट्रिंग के रूप में लौटाएं।
    """
    return ' '.join(parser._actions[0].option_strings for action in parser._actions if action.option_strings)