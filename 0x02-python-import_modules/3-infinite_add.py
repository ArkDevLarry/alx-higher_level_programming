#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the result of the addition of all arguments."""
    import sys

    sum = 0;
    args = sys.argv;
    count = len(args) - 1;
    for i in range(count):
        sum += int(args[i + 1]);

    print(sum);
