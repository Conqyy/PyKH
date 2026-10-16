from typing import List
def oddsVsEvens(num: int) -> str:
    # write your code here ^_
    x = str(num)
    counterOdd =0
    counterEven=0

    for i in x:
        y=int(i)
        if y%2==0:
            counterEven+=y
        else:
            counterOdd+=y
    if counterEven>counterOdd:
        return "even"
    elif counterOdd>counterEven:
        return "odd"
    else:
        return "equal"




print(oddsVsEvens(6321))