from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    # write your code here ^_^
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


    #selection sort
    for i in range(len(nums)):
        minn = i
        for j in range(len(nums)):
            if nums[minn] < nums[j]:
                temp = nums[minn]
                nums[minn] = nums[j]
                nums[j] = temp

    return nums


print(sortedSquares([-9,12,1,3,10]))