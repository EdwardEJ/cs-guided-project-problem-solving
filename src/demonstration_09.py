"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""
def is_even(n: int) -> bool:
    # use the `%` or modulo operator to determine if it's even or odd
    return n % 2 == 0

def get_middle(input_str):
    # Your code here
    # how do we determine if the length of a string is even or odd?
    # figure out how to get the middle characters
    # return the single middle character if the length of the string is odd
    # return the two middle characters if the length of the string is even
    if is_even(len(input_str)):
      midpoint = len(input_str) // 2
      return input_str[midpoint - 1: midpoint + 1]
    else:
      # midpoint cant be a decimal
      # round midpoint down
      midpoint = len(input_str) // 2
      return input_str[midpoint]
  
print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))

## Typescript

# function isEven (n: number): boolean | void {
#     n % 2 === 0
# }

# function getMiddle (input_str: string): string {
#     if(isEven(input_str.length)) {
#         const midpoint = input_str.length / 2
#         return input_str.slice(midpoint - 1, midpoint + 1)
#     } else {
#         const midpoint = Math.floor(input_str.length / 2)
#         return input_str.slice(midpoint, midpoint + 1)
#     }
# }