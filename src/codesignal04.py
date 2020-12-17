def csAnythingButFive(start: int, end: int) -> int:
  #given starting and ending integer of a list
  #if range has any number with a "5", remove from list
  #return length of remaining integers

  # return str(num) for num in [*range(start, end + 1)] if num != 5
  # arr = [*range(start, end + 1)]
  # newArr = []

  # for num in arr:
  #   if "5" not in str(num):
  #     newArr.append(num)
  #   else:
  #     continue
  # return len(newArr)

  new_list = []
  for i in range(start, end + 1):
    if '5' in str(i):
      continue
    else:
      new_list.append(i)
  
  return len(new_list)
  
print(csAnythingButFive(-5, 0))
print(csAnythingButFive(4, 17))