def csShortestWord(input_str: str) -> int:
    #sort the string to give back the shortest length first?
    #split the string on spaces
    #return the length of the shortest word
    sorted_str = sorted(input_str.split(), key=len)
    return len(sorted_str[0])
  
print(csShortestWord("Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live"))

print(csShortestWord("ZxuvWBoofsTUtasPIhsuCJjttHhBuuHZoxZk\tWZxAkjdCqDpML"))

print(csShortestWord("not great programmer; just good programmer with great habits."))