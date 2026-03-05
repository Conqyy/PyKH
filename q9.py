from typing import List
def removeSpecialCharacters(strParam: str) -> str:
    # write your code here ^_^
    strr = ''
    for i in strParam:
        if i != '!' and i != '@' and i != '#' and i != '$' and i != '%' and i != '?' and i != '>' and i != '<' and i != ';' and i != '.':
            strr += i
    return strr
print(removeSpecialCharacters("!Hello Wo#rld"))
