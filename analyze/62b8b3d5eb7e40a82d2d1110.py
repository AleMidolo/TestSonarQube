def _c_optimizations_available():
    try:
        import pandas._libs.lib as lib
        return lib
    except ImportError:
        try:
            import pandas._lib as lib
            return lib
        except ImportError:
            return False