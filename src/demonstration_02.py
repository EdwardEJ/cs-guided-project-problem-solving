"""
Challenge #2:

Given a list of numbers, create a function that returns the list but with each
element's index in the list added to itself. You should add 0 to the number at
index 0, add 1 to the number at index 1, etc.

Examples:
- add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
- add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
- add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]

Notes:
- The input list will only contain integers.
"""
from typing import List

def add_indexes(numbers: List[int]):
    # Your code here
    # given a list of numbers, we need to output a new list 
    # each list element is the sum of the list
    # element with its corresponding index
    # iterate through the list of numbers
      # add the current number with its index
      # push that sum to a new list

    # return [(i+value) for i,value in enumerate(numbers)]

    output = []
    for i in range(len(numbers)):
      # gets index number for this iteration
      n = numbers[i]
      sum = n + i
      output.append(sum)
    return output

print(add_indexes([0, 0, 0, 0, 0]))
print(add_indexes([1, 2, 3, 4, 5]))
print(add_indexes([5, 4, 3, 2, 1]))

## Typescript

# function add_indexes(numbers: number[]): number[] {
#     const output = [];

#     for(let i = 0; i < numbers.length; i++) {
#         const n = numbers[i]
#         const sum = n + i;
#         output.push(sum)
#     }
#     return output
# }