#!/usr/bin/python3.8

if __name__ == "__main__":
    """Print names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
