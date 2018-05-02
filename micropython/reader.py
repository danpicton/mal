import ure

class Reader:
    def __init__(self, tks):
        self.tokens = tks
        self.position = 0

    def next(self):
        return #token at position, then increment

    def peek(self):
        return #token at position, don't increment

def read_str(inp):
    tokenlist = tokenizer(inp)
    read_form(tokenlist)

def tokenizer(inp):
    out = []
    pos = 0

    while pos < len(inp):
        # skip whitespace
        if inp[pos].isspace():
            pos = pos + 1
            continue

        # tokenise ~ or ~@
        if inp[pos] =='~':
            if inp[pos+1] == '@':
                out.append('~@');
                pos = pos + 1
            else:
                out.append('~');

        # tokenise []{}()\`^@
        elif inp[pos] in ('[', ']','{', '}', '(', ')', '\'', '`', '^', '@'):
            out.append(inp[pos])

        # tokenise "string"
        elif inp[pos] == '"':
            stringtoken = ''

            stringtoken = stringtoken + ('"')
            pos = pos + 1

            while inp[pos] != '"':
                stringtoken = stringtoken + (inp[pos])
                pos = pos + 1

            stringtoken = stringtoken + ('"')
            out.append(stringtoken)
            pos = pos + 1

        # tokenise ; comments
        elif inp[pos] == ';':
            commenttoken = ';'
            pos = pos + 1

            while True:
                # break on end of line or end of input
                if pos == len(inp) or inp[pos] == '\n':
                    break

                commenttoken = commenttoken + (inp[pos])
                pos = pos + 1

            out.append(commenttoken)
            pos = pos + 1

        # tokenise symbols: a, b, etc, numbers, true, false, nil
        elif ure.match('[\[\]{}(\'"`,;)]', inp[pos]) is None :
            out.append(inp[pos])

        pos = pos + 1
    
    return out
