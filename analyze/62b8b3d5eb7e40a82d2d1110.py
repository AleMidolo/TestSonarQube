def _c_optimizations_available():
    """
    Return the C optimization module, if available, otherwise
    a false value.

    If the optimizations are required but not available, this
    raises the ImportError.

    This does not say whether they should be used or not.
    """
    try:
        import c_optimizations  # Assuming the module is named c_optimizations
        return c_optimizations
    except ImportError:
        raise ImportError("C optimization module is required but not available.")