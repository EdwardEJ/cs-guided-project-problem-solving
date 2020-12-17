from typing import List

def positive_num(element: int) -> int:
  return element > 0

def csSumOfPositive(input_arr: List[int]) -> int:
    #use only positive numbers from List of integers
    #add filtered list of positive numbers
    #return the sum positive integers
    #if no positive numbers, return 0
    return sum(filter(positive_num, input_arr))

print(csSumOfPositive([1, 2, 3, -4, 5]))
