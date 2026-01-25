# Q1 Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
s = "loveletcode"
def first_unique_charecter(s:str):
  unique_char = {}  
  for char in s:
    unique_char.get(char,0) +1 
  
  for i in range(len(s)):
    if unique_char[s[i]] == 1:
      return i
  return -1

# Q 22 Given an input string s, reverse the order of the words. Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words.

s = " hello world "
def reverse_worlds(s):
  s1 = s.split()
  return "".join(s1[::-1])

#q23 group of anagram
s = ["eat", "tea", "tan", "ate", "nat", "bat"]
def group_of_anagram(s):
  group_ana = {}
  for i in s:
    if "".join(sorted(i)) not in group_ana:
      group_ana["".join(sorted(i))] = [i]
    else:
      group_ana["".join(sorted(i))].append(i)
  return group_ana.values()

# print(group_of_anagram(s))

# Q24 Find the "Kth" Largest Element
#Problem: Given an integer array nums and an integer k, return the kth largest element in the array.
nums = [3,2,3,1,2,4,5,5,6]
k = 4

def kth_largest(nums,k):
  s = sorted(nums)
  return s[len(s)-k]
  pass
# print(kth_largest(nums,k))

# Q25 spiral order for that 
# yeh nahi ho raha hain baad main try karenge
# s = [[1,2,3],[4,5,6],[7,8,9]]
# ans = []
# total = len(s)
# i = 0
# j = 0
# # for left to right jane ke liye
# while True:
#   if j < len(s):
#     ans.append(s[i][j])
#     j+=1
#   else:
#     break
# # for downword direction
# i+=1
# j -= 1
# while True:
#   if i < len(s):
#     ans.append(s[i][j])
#     i+=1
#   else:
#     break
# # piche mudane ke liye
# i -= 1
# j-=1
# print(i,j)
# while True:
#   if j < 0:
#     ans.append(s[i][j])
#     j -= 1
#   else:
#     break

# print(i,j)
# print(ans)


#Container With Most Water
# Problem: Given an array height representing the height of lines, find two lines that together with the x-axis form a container, such that the container contains the most water.

s = [1,8,6,2,5,4,8,3,7]
left = 0
right = 0
for i in range(len(s)):
  pass

"""
a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""

def equal_pairs(grid):
    n = len(grid)
    row_counts = {}
    count = 0
    for row in grid:
        row_tuple = tuple(row)
        row_counts[row_tuple] = row_counts.get(row_tuple, 0) + 1
    for j in range(n):
        column = tuple(grid[i][j] for i in range(n))
        if column in row_counts:
            count += row_counts[column]
            
    return count
# grid = [[3,2,1],[1,7,6],[2,7,7]]
# print(f"Total Equal Pairs: {equal_pairs(grid)}")

"""
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
"""

s = "leet**cod*e"
stack =[]
for i in s:
  if i != '*':
     stack.append(i)
  else:
     stack.pop()
print(stack)
      
   





