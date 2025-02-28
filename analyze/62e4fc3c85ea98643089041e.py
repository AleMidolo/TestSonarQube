def _inline_r_setup(code: str) -> str:
    """
    R के कुछ व्यवहारों को env वेरिएबल्स के माध्यम से कॉन्फ़िगर नहीं किया जा सकता है,
    लेकिन केवल R शुरू होने के बाद R विकल्पों के माध्यम से कॉन्फ़िगर किया जा सकता है।
    इन्हें यहां सेट किया गया है।
    """
    setup_code = """
    options(repos = c(CRAN = "https://cloud.r-project.org"))
    options(warn = 1)
    options(stringsAsFactors = FALSE)
    """
    return setup_code + code