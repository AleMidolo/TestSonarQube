def make_find_paths(find_paths):
    """
    `--find` के लिए पास किए गए पथ खंडों (path fragments) या पैटर्न के अनुक्रम को लें और सभी पथ खंडों को ग्लोब पैटर्न में बदलें। मौजूदा पैटर्न को बिना बदले पास करें।

    उदाहरण के लिए, यदि `find_paths` है:

    ['foo.txt', 'pp:root/somedir']

    ... तो इसे इस प्रकार बदलें:

    ['sh:**/*foo.txt*/**', 'pp:root/somedir']
    """
    return ['sh:**/*' + path_fragment + '*/**' if not path_fragment.startswith(('pp:', 'sh:')) else path_fragment for path_fragment in find_paths]