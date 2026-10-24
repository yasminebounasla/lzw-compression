from compression import initial_dictionary


def lzw_decompress(codes):
    table = list(initial_dictionary())      # convert the dict to a list: index = code

    if not codes:                           # nothing to decompress
        return "", initial_dictionary()

    # if codes[0] isn't 0, 1 or 2
    if not 0 <= codes[0] < len(table):
        raise ValueError(f"Invalid first code: {codes[0]}")

    w = table[codes[0]]                     # w = decode(first code)
    result = [w]                            

    for k in codes[1:]:                     # the first one is already decoded
        if 0 <= k < len(table):             # decode(k) exists in the dictionary
            decoded_k = table[k]
        elif k == len(table):               # special case: decode(k) is not in the dictionary yet
            decoded_k = w + w[0]           
        else:                               # impossible code
            raise ValueError(f"Invalid code: {k}")

        result.append(decoded_k)            # add decode(k) to the result

        new_substring = w + decoded_k[0]    # w + first character of decode(k)
        if new_substring not in table:      # always true for a valid stream
            table.append(new_substring)     # it gets the next free code

        w = decoded_k                       # decode(k) becomes the previous piece

    # list -> dict {substring: code}, same format as the compression
    dictionary = {substring: code for code, substring in enumerate(table)}
    return "".join(result), dictionary