"""
xyz_there
Source:https://codingbat.com/prob/p149391

Question:
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a 
period (.). So "xxyz" counts but "x.xyz" does not.

Example:
xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True

Goal: Return True if the given string contains an appearance of "xyz" where the 
      xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" 
      does not.

"""


def xyz_there(str):
    if str[:3] == "xyz":
        return True
                    
    for i in range(1, len(str) - 2):
        if str[i-1] != "." and str[i:i+3] == "xyz":
            return True
                     