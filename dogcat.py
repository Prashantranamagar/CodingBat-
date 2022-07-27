"""
Dog Cat Count
Source:https://codingbat.com/prob/p164876

Question:Return True if the string "cat" and "dog" appear the same number of times in the given string.

Example:
cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

"""

def cat_dog(str):
  catcount = 0
  dogcount = 0
  
  for i in range(len(str)):
    if str[i:i+3] == 'dog':
      dogcount += 1
    if str[i:i+3] == 'cat':
      catcount += 1
  if dogcount == catcount:
    return True
    
  return False