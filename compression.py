
def initial_dictionary():
    return {"a": 0, "b": 1, "c": 2}


def lzw_compress(text):
    dictionary = initial_dictionary() 
    w = ""          # current known substring
    codes = []

    for k in text:  # read one character at a time
        wk = w + k
        if wk in dictionary:
            w = wk                              # keep extending the match
        else:
            codes.append(dictionary[w])         # output the code of w
            dictionary[wk] = len(dictionary)    # add wk with the next free code
            w = k                               # restart from the current character

    if w:                                       # end of input: output the last w
        codes.append(dictionary[w])

    return codes, dictionary