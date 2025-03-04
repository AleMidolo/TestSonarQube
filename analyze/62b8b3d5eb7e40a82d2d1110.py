def _c_optimizations_available():
    """
    Return the C optimization module, if available, otherwise
    a false value.

    If the optimizations are required but not available, this
    raises the ImportError.

    This does not say whether they should be used or not.
    """
    try:
        import _speedups
        return _speedups
    except ImportError:
        return False