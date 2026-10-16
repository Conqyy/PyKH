from typing import List
def calculateContributions(totalDonation: float, weights: List[float]) -> List[float]:
    # write your code here ^_^
    totalweight = []
    totalw =0

    for i in weights:
        totalw+=i

    for i in range(len(weights)):
        totalweight.append((weights[i]/totalw)*totalDonation)
        totalweight[i] = round(totalweight[i],2)

    return totalweight

print(calculateContributions(500, [1,1,1]))