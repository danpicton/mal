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
    tokens = tokenizer(inp)
    reader = Reader(tokens)
    read_form(reader)

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
            othertoken = ''

            while True:
                if pos == len(inp) or ure.match('[\[\]{}(\'"`,;)]', inp[pos]) is not None:
                    break
                
                othertoken = othertoken + inp[pos]
                pos = pos  + 1

            out.append(othertoken)
            continue

        pos = pos + 1
    
    return out

def read_form(reader):
    currchar = reader.peek()

    if currchar == '(':
        read_list(reader)
    else:
        read_atom(reader)

def read_list(reader):
    out = []

    while reader.peek() != ')':
        out.append(reader.next())

    return out.append(')')

def read_atom(reader):
    return True # HERE
