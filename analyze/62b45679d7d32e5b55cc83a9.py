def parser_flags(parser):
    """
    दिए गए argparse.ArgumentParser इंस्टेंस के लिए, इसके आर्गुमेंट फ्लैग्स को एक स्पेस-सेपरेटेड 
    स्ट्रिंग के रूप में रिटर्न करें।
    """
    return ' '.join(parser._option_string_actions.keys())