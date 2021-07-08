def auto_string(cls: object) -> str:
    return f'{type(cls).__name__}({", ".join("{}={}".format(*item) for item in vars(cls).items())})'
