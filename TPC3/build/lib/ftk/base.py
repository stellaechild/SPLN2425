import re
import jjcli


def lexer(txt):
    # FIXME - patterns stopwords lemas YET TO BE TREATED
    return re.findall(r'\w+(-\w+)*|[^\w\s]+',txt)


def main():
    cl = jjcli.clfilter()
    for txt in cl.text():
        print(lexer(txt))
