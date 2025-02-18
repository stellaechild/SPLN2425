import re
import jjcli
from collections import Counter

def lexer(txt):
    # FIXME - patterns stopwords lemas YET TO BE TREATED
    return re.findall(r'\w+(-\w+)*|[^\w\s]+',txt)

def counter(tokens):
    return Counter(*tokens) # FIXME

def main():
    cl = jjcli.clfilter()
    tokens = []
    for txt in cl.text():
        t = lexer(txt)
        print(t)
        tokens.append(t)
    c = counter(t)
    print(c)