"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""
from typing import List

def last(a: List[int], n: int) -> List[int]:
    # Your code here
    # if n longer than length of list, return `invalid`
    # return the last n elements as a string of ints
    # how would we do this if we just needed to return the first n elements?
    # we'd grab everything from index 0 up to n
      # grab a subslice where that subslice starts at the beginning and has length n
    # Python's slicing syntax
    # a[0:n] - get first n elements
    # a[len(a)-n:]
    # we want to start slicing the len(a) - n and then take everything from there to the end of the list
    if n > len(a):
      return 'Invalid'

    last_n = a[len(a) - n:]
    return last_n

## Typescript

# function last(a: number[], n: number): number[] | string {
#     if (n > a.length) return 'invalid';

#     const last_n = a.slice(a.length -n)
#     return last_n;
# }