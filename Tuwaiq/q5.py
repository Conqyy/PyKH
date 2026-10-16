from typing import List
def calculateTotalFastingTime(startTimes: List[str], endTimes: List[str]) -> float:
    # write your code here ^_^
    day1start = startTimes[0].split(':')
    day2start = startTimes[1].split(':')
    day1end = endTimes[0].split(':')
    day2end = endTimes[1].split(':')
    day1Total = float(day1end[0])+float(float(day1end[1])/100)
    day2Total = float(day2end[0])+float(float(day2end[1])/100)
    day1Total -= float(day1start[0])+float(float(day1start[1])/100)
    day2Total -= float(day2start[0])+float(float(day2start[1])/100)
    


    return day1Total+day2Total


print(calculateTotalFastingTime(["04:30","05:00"],["18:30","18:00"]))