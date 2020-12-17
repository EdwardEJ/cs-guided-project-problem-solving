def csLongestPossible(str_1: str, str_2: str) -> str:
  #receive two strings
  #iterate through strings and filter once occuring characters
  #return filtered string
  sorted_once_occuring_string = ''
  
  for char in sorted((str_1 + str_2)):
    if char in sorted_once_occuring_string:
      continue
    else:
      sorted_once_occuring_string += char

  return sorted_once_occuring_string

print(csLongestPossible("aretheyhere", "yestheyarehere"))