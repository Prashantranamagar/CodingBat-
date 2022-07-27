"""
Count hi
Source:https://codingbat.com/prob/p167246

Question:
Return the number of times that the string "hi" appears anywhere in the given string.

Examples:
count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2

"""

def count_hi(str):
  result = 0
  for i in range(len(str)):
    
    if str[i:i+2] == 'hi':
      result = result+1
  return result
