from typing import (
    List,
)


class Solution:
    """
    @param cars: integer array of length denoting the parking slots where cars are parked
    @param k: integer denoting the number of cars that have to be covered by the roof
    @return: return the minium length of the roof that would cover k cars
    """

    def parking_dilemma(self, cars: List[int], k: int) -> int:
        # write your code here
        cars.sort()
        n = len(cars)
        minL = cars[k-1] - cars[0]

        for i in range(0, n-k+1):
            if minL > cars[i+k-1] - cars[i]:
                minL = cars[i+k-1] - cars[i]
        return minL + 1
