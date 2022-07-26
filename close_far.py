"""
close_far
Source:https://codingbat.com/prob/p160533

Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the 
other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of 
a number.

Examples:
close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True

Goal: Find absolute diffrence of ab, bc , ac
      return True if {ab<=1 and ac>=2 and bc>=2)  or (ac <= 1 and bc>=2 and ab >=2)  
      else return False

"""


def close_far(a, b, c):
  ab = abs(a-b)
  ac = abs(a-c)
  bc = abs(b-c)
  
  if  (ab <= 1 and (ac>=2 and bc >=2)) or (ac <= 1 and (bc>=2 and ab >=2)) :  
    return True
  else:
    return False
