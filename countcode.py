"""
Count Code
Source:https://codingbat.com/prob/p186048

Question:Return the number of times that the string "code" appears anywhere in the given string, except 
we'll accept any letter for the 'd', so "cope" and "cooe" count.

Example:
count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2

"""


def count_code(str):
  result = 0
  for i in range(len(str)-3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      result +=1
  return result
