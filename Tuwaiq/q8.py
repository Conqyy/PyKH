from typing import List
def countdown(num: int) -> List[int]:
    # write your code here ^_^
    tlist  =[]

    if num<3:
        return [0]
    else:

        for i in range(num-3 , -1 , -3):
            if i!=0 and i%2==0:
                tlist.append(i)
        tlist.sort()
        return tlist

