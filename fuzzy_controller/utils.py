import inspect


def get_function_source(fn):
    """
    Prints the full source code of a given function.

    Usage:
        get_function_source(fuzzify)
    """
    try:
        source_code = inspect.getsource(fn)
        print(f"\nFunction: {fn.__name__}\n")
        print(source_code)
    except TypeError:
        print("Invalid function provided.")
    except Exception as e:
        print(f"Error: {e}")
