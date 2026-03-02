from typing import List


def findDonationTargetDay(donations: List[float], target: float) -> int:
    # write your code here ^_^
    acc = 0.0
    day = 1
    for i in donations:
        acc += i
        if acc >= target:
            break
        else:
            day += 1
    if acc < target:
        day = -1
    return day
