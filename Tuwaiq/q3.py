from typing import List


def oct_to_bin(octal: int) -> str:
    # write your code here ^_^
    nums = str(octal)
    binums = ""
    for i in nums:
        n = int(i)
        if n == 0:
            binums += "000"
        elif n == 1:
            binums += "001"
        elif n == 2:
            binums += "010"
        elif n == 3:
            binums += "011"
        elif n == 4:
            binums += "100"
        elif n == 5:
            binums += "101"
        elif n == 6:
            binums += "110"
        elif n == 7:
            binums += "111"
    z=""
    for i in binums:
        zz= int(i)
        if zz!=0:
            break
        else:
            z+='0'

    binums=binums.strip(z)
    return binums
print(oct_to_bin(123))

