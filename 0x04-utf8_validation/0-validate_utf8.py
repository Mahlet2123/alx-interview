#!/usr/bin/python3
""" 0-validate_utf8 module """


def validUTF8(data):
    """
    a method that determines if a given data set
    represents a valid UTF-8 encoding.
    """
    for i in data:
        if i in range (0, 255):
            continue
        else:
            return False
    return True
