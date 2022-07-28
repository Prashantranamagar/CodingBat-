"""
End Other
Source:https://codingbat.com/prob/p174314

Question:Given two strings, return True if either of the strings appears at the very end of the other string,
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
Note: s.lower() returns the lowercase version of a string.

Example:
end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True

"""


def end_other(a, b):
  lengtha = -1*len(a)
  lengthb = -1*len(b)
  
  if a.lower() == b[lengtha:].lower() or b.lower() == a[lengthb:].lower():
    return True
    
  return False
