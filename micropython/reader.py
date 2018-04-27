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

    while pos < range(len(inp)):
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
        elif false:
            return 1

        # tokenise ; comments
        elif false:
            return 1

        # tokenise symbols: a, b, etc, true, false, nil
        elif false:
            return 1

        pos = pos + 1

# HERE *********************************************

    # madregex = ure.compile('[\s,]*(~@|[\[\]{}()\\\'`~^@]|"(?:\\.|[^\\"])*"|;.*|[^\s\[\]{}(\\\'"`,;)]*)')
    # blah = ure.search(madregex, inp)
    # blah = ure.search(r"[\s,]*(~@|[\[\]{}()'`~^@]|\"(?:\\.|[^\"])*\"|;.*|[^\s\[\]{}('\"`,;)]*)", inp)
    blah = ure.search(r"[\s,]*(~@|[{}()'`~^@])", inp)
    #[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"|;.*|[^\s\[\]{}('"`,;)]*)
    return blah.group(1)

