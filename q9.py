from typing import List
def removeSpecialCharacters(strParam: str) -> str:
    # write your code here ^_^

    strp = strParam.strip('!')
    strp = strp.strip('@')
    strp = strp.strip('#')
    strp = strp.strip('#')

    return strp

print(removeSpecialCharacters("!Hello Wo#rld"))
