"""
Make Chocolate.
Source:https://codingbat.com/prob/p190859

We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos 
each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 
if it can't be done.

Example:
make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2

"""


def make_chocolate(small, big, goal):
  if 5*big +small < goal:
    return -1
     
  modulos = goal % 5  # modulos gives the reminder
  quetient = goal // 5
  
  if 5*quetient +small < goal:
    return -1
    
  if quetient *5 > 5*big:
    c = goal - 5*big 
    return c  
    
  if 5*quetient + modulos == goal:
    return modulos
    
 