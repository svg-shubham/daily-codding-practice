# sliding window problems
# An integer array nums and an integer k.
# Find the maximum sum of any contiguous subarray of size k.

nums = [2,1,5,1,3,2]
k = 3
def find_max_sub_array(nums:list,k):
  first = 0
  last = first + k
  sum_sub_array = sum(nums[first:last])
  max_sum = sum_sub_array
  for i in range(k,len(nums)):
    sum_sub_array = sum_sub_array - nums[i-k] + nums[i]
    max_sum = max(max_sum,sum_sub_array)
  return max_sum

  
# problem 2 
"""
Maximum Average Subarray
An integer array nums and integer k.
Return the maximum average of any contiguous subarray of size k.
"""

nums = [1,12,-5,-6,50,3]
k = 4

def avg_sub_array(nums : list,k:int):
  window_sum = sum(nums[:k])
  max_sum = window_sum
  for i in range(k,len(nums)):
    window_sum = window_sum - nums[i-k] + nums [i]
    max_sum = max(max_sum,window_sum)
  return max_sum / k

# print(avg_sub_array(nums,k))

"""
Count Occurrences of a Number
Array nums, integer k, integer x.
Count how many subarrays of size k have sum greater than or equal to x.
"""
nums = [2,2,2,2,5,5,5,8]
k = 3
x = 10

def find_count_sub_more_than(nums:list,k:int,x:int):
  window_sum = sum(nums[:k])
  count = 1 if window_sum > x else 0
  for i in range(k,len(nums)):
    window_sum = window_sum - nums[i-k] + nums[i]
    if window_sum >= x:
      count +=1
    else:
      pass
  return count

# print(find_count_sub_more_than(nums,k,x))

"""problem number 4
    Longest Subarray with Sum ≤ K
    Array nums and integer k.

    Task:
    Find length of longest contiguous subarray whose sum ≤ k.
"""

nums = [2,1,3,4,1,1,1]
k = 5

def find_length_subarray(nums:list,k:int):
  left = 0
  window_sum = 0
  max_len = 0
  for right in range(len(nums)):
    window_sum += nums[right]

    while window_sum > k:
      window_sum -= nums[left]
      left += 1
    max_len = max(max_len,right - left +1)
  return max_len
  

# print(find_length_subarray(nums,k))

"""
Problem 5: Longest Substring Without Repeating Characters
"""
s = "abcabcbb"

def find_substring_without_rep_ele(s:str):
  char_set = set()
  max_len = 0
  left = 0
  for right in range(len(s)):
    while s[right] in char_set:
      char_set.remove(s[left])
      left += 1
    char_set.add(s[right])
    max_len = max(max_len,right-left+1)
  return max_len


  
# print(find_substring_without_rep_ele(s))
"""
Problem 6: Maximum Number of Vowels in a Substring of Given Length
Given a string s and an integer k, return the maximum number of vowels in any substring of length k.
Vowels: a, e, i, o, u
Substring continuous honi chahiye
Window size fixed (k) hai
"""
s = "abciiidef"
k = 3

def max_num_vowels_in_sub_str(s:str,k:int):
  vowels = "aeiou"
  count = 0
  for i in s[:k]:
    if i in vowels:
      count += 1
  max_vowels = count
  for right in range(k,len(s)):
    if s[right - k] in vowels:
      count -=1

    if s[right] in vowels:
      count +=1

    max_vowels = max(max_vowels,count)
  return max_vowels
  pass
      
      
# print(max_num_vowels_in_sub_str(s,k))
      


    
# for mindstrex ke ponitof view se codding qutions
"""
Challenge A: String Compression

Input: "aaabbccaa"

Output: "a3b2c2a2"

Logic: Loop chalao aur counter rakho jab tak character badal na jaye.

Challenge B: Merge Two Sorted Lists

Input: [1, 3, 5] and [2, 4, 6]

Output: [1, 2, 3, 4, 5, 6]

Logic: Bina sort() function use kiye isse kaise karoge? (Hint: Two-pointer approach).

Challenge C: Fibonacci using Recursion vs Loop

Woh puchenge ki Recursion kab use karna hai aur Loop kab.

Logic: Recursion mein memory (Stack) zyada lagti hai, toh bade numbers ke liye Loop (Iterative) ya Memoization achha hai."""
s = "aaabbccaa"

def string_comprehenssion(s:str):
  if not s : return ""
  result = ""
  temp = s[0]
  count = 1
  for x in s[1::]:
    if x == temp : 
      count += 1
    else:
      result += temp + str(count)
      temp = x
      count = 1
  result += temp + str(count)
  return result if len(result) < len(s) else s

# print(string_comprehenssion(s))

# Input: [1, 3, 5] and [2, 4, 6]

# Output: [1, 2, 3, 4, 5, 6]

# Logic: Bina sort() function use kiye isse kaise karoge? (Hint: Two-pointer approach).

a = [1, 3, 5] 
b = [2, 4, 6]

# def sorted_array(a:list,b:list):
#   result = []
#   first = 0
#   last = 0
#   for i in range(len(a)):
#     if a[i] < b[i]:
#       result.append(a[i])
#       result.append(b[i])
#     else:
#       result.append(b[i])
#       result.append(a[i])

#   return result

# print(sorted_array(a,b))

def merge_sorted_lists(a, b):
    result = []
    i = 0  # Pointer for list 'a'
    j = 0  # Pointer for list 'b'

    # Jab tak dono lists mein elements bache hain
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # Agar list 'a' mein kuch bacha hai (b khatam ho gayi)
    while i < len(a):
        result.append(a[i])
        i += 1

    # Agar list 'b' mein kuch bacha hai (a khatam ho gayi)
    while j < len(b):
        result.append(b[j])
        j += 1

    return result
# print(merge_sorted_lists(a,b))

def febonacci_loop(n):
  a,b = 0,1
  for i in range(n):
    print(a,end = " ")
    a,b = b,a+b
  
# print(febonacci_loop(10))

def febonacci_recurssive(n):
  if n <= 1:
    return n
  else:
    return febonacci_recurssive(n-1) + febonacci_recurssive(n-2)

# print(febonacci_recurssive(10))

s = "programming"
# def find_duplicate(s:str):
#   d = {}
#   l = []
#   for i in s:
#     if i not in d:
#       d[i] = 1
#     else:
#       d[i]+=1
#   for x in d:
#     if d[x] > 1:
#       l.append(x)

#   return " ".join(l)


def find_duplicate(s:str):
  d = {}
  duplicate =[]
  for x in s:
    d[x] = d.get(x,0) +1
  for char,count in d.items():
    if count > 1 :
      duplicate.append(char)
  return " ".join(duplicate)
# print(find_duplicate(s))

# move all zero at one side 
l = [0, 1, 0, 3, 12]

def move_zero(l:list):
  pos = 0
  for i in range(len(l)):
    if l[i] != 0:
      l[pos] = l[i]
      pos += 1
  while pos < len(l):
    l[pos] = 0
    pos +=1 
  return l


# print(move_zero(l))

l1 = [1, 2, 4, 5, 6] 
n=6


def check_for_missing_number(l1,n):
  sum1 = sum(l1)
  t = n+1
  actual_sum = (n*t)/2
  # print(actual_sum)
  return int(actual_sum - sum1)

# print(check_for_missing_number(l1,n))
D1= {'apple': 10, 'banana': 5}

D2= {'apple': 5, 'orange': 8}

def merge_dict(d1,d2):
  result = d1.copy()
  for i in d2:
    if i in result:
      result[i] += d2[i]
    else:
      result[i]=d2[i]
  return result

# print(merge_dict(D1,D2))

l1 = [1, [2, 3], [[4, 5], 6]]
def list_flatner(input_list, result=None):
    if result is None:
        result = []
    
    for i in input_list:
        if isinstance(i, list):
            list_flatner(i, result) 
        else:
            result.append(i)
            
    return result

# print(list_flatner(l1))

# Tujhe ek list di gayi hai jo ek stock (ya product) ki price batati hai alag-alag din par. Tujhe batana hai ki sabse zyada profit kab hota agar tu ek din kharidta aur baad mein bechta.

inp = [7, 1, 5, 3, 6, 4]

def margin_cal(prices:list):
  if not prices:
    return 0
  min_price = float('inf')
  max_profit = 0
  for price in prices:
    if price < min_price:
      min_price = price
    elif price - min_price > max_profit:
      max_profit = price - min_price
  return max_profit
  
# print(margin_cal(inp))

s = "A man, a plan, a canal: Panama"
# s = s.split(" ")
# s1 = " ".join(i.lower() for i in s if i.isalnum() )
# print(s1 == s1[::-1])
# print(s1[::-1])

def pallindrome(s:str):
  s1 = " ".join(i.lower() for i in s if i.isalnum)
  return s1 == s1[::-1]

l = [1, 2, 2, 3, 4, 4, 5, 1]

def remove_duplicate(l):
  seen = set()
  res = []
  for i in l:
    if i not in seen:
      seen.add(i)
      res.append(i)
    else:
      pass
  return res


inp = ["eat", "tea", "tan", "ate", "nat", "bat"]

def bhai_kya_naam_du(inp:list):
  result_dict = {}
  for i in range(len(inp)):
    temp = "".join(sorted(inp[i]))
    print(temp)
    if temp not in result_dict:
      result_dict[temp]= [inp[i]]
    else:
      result_dict[temp].append(inp[i])
  result = [ i for i in result_dict.values()]

  return result

# print(bhai_kya_naam_du(inp))

import math

def is_prime(num):
    if num < 2: return False 
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False 
            
    return True 

def check_in_range(num1, num2):
    return [i for i in range(num1, num2 + 1) if is_prime(i)]

print(check_in_range(10, 20))

