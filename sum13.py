"""
Sum 13
Source:https://codingbat.com/prob/p167025

Question:
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very 
unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

Examples:
sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6

Goal: Find total sum
      if i = 13 then skip i and i+1

"""


def sum13(nums):
  arrsum = 0
  i=0
  
  while i< len(nums):
    if nums[i] == 13:
      i+=1
    else:  
      arrsum += nums[i]  
    i+= 1
  return arrsum 