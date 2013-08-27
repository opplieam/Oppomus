# -*- coding: utf-8 -*-


def smart_trim(data, length, suffix='...'):
    """
    Return a trim data. The algorithm is to find the space from length argument down to 0.
    If not found, It's will seek from length to the last character.

    Keyword Arguments:
    data -> (String) A data to be trim. Ex. 'Hello world'
    length -> (Integer) A length of data to be trim. Ex. 5
    suffix -> (String) A suffix after trim successful. Default is '...'

    Usage:
    print smart_trim('Hello world Opponent', 5)
    Output: Hello...
    print smart_trim('Hello world Opponent', 15)
    Output: Hello world...
    """
    if len(data) >= length:
        try:
            index = data.rindex(' ', 0, length)
            data = data[:index] + suffix
        except ValueError:
            try:
                index = data.index(' ', length)
                data = data[:index] + suffix
            except ValueError:
                #can not trim
                pass
    return data