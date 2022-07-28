""""
Sum 67
Source:https://codingbat.com/prob/p108886

Question:Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and 
extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

Example:
sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4

Goal: Initilize sum and flag to set the track of numbers initally flag is true
      if the number is 6 set it to False until u find seven
      i.e elif the flag is false and number 7 set it back to true
      elif flae is true calculate sum 

"""

def sum67(nums):
  flag = True
  sum = 0
  for i in range(len(nums)):
    if nums[i] == 6:
      flag = False
    elif flag ==False and nums[i] == 7:
      flag = True
    elif flag == True:
      sum += nums[i]
  return sum
