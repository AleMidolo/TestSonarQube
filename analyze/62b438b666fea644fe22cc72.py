def parser_flags(parser):
    """
    दिए गए argparse.ArgumentParser इंस्टेंस के लिए, इसके आर्गुमेंट फ्लैग्स को एक स्पेस-सेपरेटेड 
    स्ट्रिंग के रूप में रिटर्न करें।

    return " ".join([action.option_strings[0] for action in parser._actions if action.option_strings])
    """
    return " ".join([action.option_strings[0] for action in parser._actions if action.option_strings)