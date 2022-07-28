"""
Centered Average
Source:https://codingbat.com/prob/p126968

Question:
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except 
ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, 
ignore just one copy, and likewise for the largest value. Use int division to produce the final average. 
You may assume that the array is length 3 or more.

Example:
centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3

"""

def centered_average(nums):
  large = nums[0]
  small = nums[0]
  totalsum = nums[0]
  for i in range(1, len(nums)):
    large = max(large, nums[i])
    small = min(small, nums[i])
    totalsum += nums[i]
  
  average = (totalsum - large -small)/(len(nums)-2)
  return average
  