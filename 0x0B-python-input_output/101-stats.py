#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""


def print_stats(size, status_codes):
    """
    print_stats - reads stdin line by line and computes metric

    args - size: The size of the file read.
        status_codes: number of lines of status_code
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    """
    Any code under this code will not be included when this
    file is imported as a module

    """
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    counter = 0

    try:
        for n_line in sys.stdin:
            if counter == 10:
                print_stats(size, status_codes)
                counter = 1
            else:
                counter += 1

            n_line = n_line.split()

            try:
                size += int(n_line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if n_line[-2] in valid_codes:
                    if status_codes.get(n_line[-2], -1) == -1:
                        status_codes[n_line[-2]] = 1
                    else:
                        status_codes[n_line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
