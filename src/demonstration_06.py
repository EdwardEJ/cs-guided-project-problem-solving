"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str: str) -> int:
    # Your code here
    # keep a list or a string of all the vowels we care about
    # count number of vowels
      # keep a counter to keep track number of vowels
      # we need to inspect every character in the input string
      # as we iterate, check if there current character is part of the vowel string/list
      # if it is, increment counter
    #return counter
    num_vowels = 0
    vowels = 'aeiou'

    for char in input_str:
      if char in vowels:
        num_vowels += 1

    return num_vowels

print(get_count('aewoi'))

## Typescript

# function getCount (input_str: string): number {
#     let numVowels = 0;
#     const vowels = 'aeoiu';

#     for (let i = 0; i < input_str.length; i++) {
#         const char = input_str[i]
#         if(vowels.includes(char)) {
#             numVowels += 1
#         }
#     }
#     return numVowels
# }