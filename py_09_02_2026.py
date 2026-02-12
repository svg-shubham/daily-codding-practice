# The "Two-Sum" Logic: Given a list of prices, find two items that sum exactly to a target budget. Can you do this in $O(n)$ time?
"""
1. The "Two-Sum" LogicThe Goal: Find two numbers that sum to a target in $O(n)$ time using a Hashmap (Dictionary).
Test Case A (Standard): prices = [10, 20, 30, 40], target = 50.
Result: [10, 40] or indices [0, 3].
Test Case B (No Solution): prices = [1, 2, 3], target = 7.
Result: Return None or an empty list.
Test Case C (Same Number Twice): prices = [10, 20, 25, 40], target = 50.
Constraint: You cannot use the index of 25 twice to make 50. 
You must find two distinct elements.
Test Case D (Negative Prices/Offsets): prices = [-10, 20, 30], target = 10."""
prices = [10, 20, 30, 40]
target = 50

def two_sum(prices, target):
    seen = {} # Number: Index
    for i, num in enumerate(prices):
        needed = target - num
        if needed in seen:
            return [seen[needed], i] # Purana index aur current index
        seen[num] = i
    return None


"""
2. Merging Intervals
The Goal: Combine overlapping time slots so your inventory/warehouse schedule isn't double-booked.
Test Case A (Contained): [[1, 10], [2, 5]].Logic: Since [2, 5] is entirely inside [1, 10], 
the result is just [[1, 10]].Test Case B (Sequential/Touching): [[1, 3], [3, 6]].Logic: They meet at 3. Should they merge? (Usually yes, to [[1, 6]]).Test Case C (No Overlap): [[1, 2], [5, 6]].Result: Stay the same: [[1, 2], [5, 6]].Test Case D (Unsorted Input): [[8, 10], [1, 3], [2, 6]].Note: You must sort by the start time first to solve this in $O(n \log n)$.
"""

# Find the K-th Largest Element
# Standard: nums = [3,2,1,5,6,4], k = 2 (Ans: 5)

#  i want to find kth largest number so for that i need to function 

def find_k_number(arr:list,k:int):
    if k > len(arr) or k < 0:
        return "abe yedz.... barobar tak"
    arr.sort()
    return arr[len(arr) - k]

# move all zeros
def move_zero(arr:list):
    res = []
    count = 0
    for i in arr:
        if i != 0:
            res.append(i)
        else:
            count += 1
    return res + [0] * count

# . Find Duplicates ($O(n)$ time)Multiple Duplicates: [4,3,2,7,8,2,3,1] (Ans: [2,3])No Duplicates: [1,2,3,4,5] (Ans: [])All Same: [1,1,1,1] (Ans: [1])Negative Numbers: [-1, 2, -1, 3, 2] (Ans: [-1, 2])

def find_duplicates(arr:list):
    dic = {}
    for i in arr:
        dic[i] = dic.get(i,0) +1
    return [i for i in dic if dic[i] > 1]

# Standard: l1 = [1,2,4], l2 = [1,3,4] (Ans: [1,1,2,3,4,4])
# Uneven Length: l1 = [1,2], l2 = [3,4,5,6] (Ans: [1,2,3,4,5,6])
# One Empty: l1 = [], l2 = [0] (Ans: [0])
# Different Ranges: l1 = [1,3,5], l2 = [10,20] (Ans: [1,3,5,10,20])

def merge_two_sorted(arr1:list,arr2:list):
    arr = arr1 + arr2
    return sorted(arr)

# . Rotate an Array (k steps)
# Standard: nums = [1,2,3,4,5,6,7], k = 3 (Ans: [5,6,7,1,2,3,4])
# K is 0: nums = [1,2,3], k = 0 (Ans: [1,2,3])
# K > Length: nums = [1,2], k = 5 (Ans: [2,1] — Hint: Use k % len)
# Negative K (Optional): nums = [1,2,3,4,5], k = -1 (Should rotate left)

def rotate_from_k_pos(arr:list,k:int):
    first_part = arr[0:k+1]
    last_part = arr[k+1::]
    return last_part + first_part

"""
Find the Missing Number
Missing in Middle: [3,0,1] (Ans: 2)

Missing Zero: [1,2,3] (Ans: 0)

Missing Last: [0,1,2] (Ans: 3)

Large Range: nums = [0, 1, ..., 100] minus one number.
"""
"""
8. Container With Most Water
Standard: [1,8,6,2,5,4,8,3,7] (Ans: 49)

Flat Ground: [1,1] (Ans: 1)

Descending: [5,4,3,2,1] (Ans: 6)

Mountain Shape: [1,2,4,3,2,1] (Ans: 6)

All the best for the coding, bhai! Kya tu chahta hai main Category 2 (Strings) ke bhi test cases ready kar doon?"""

def max_water(arr:list[int]) -> int:
    max_water = 0
    left = 0
    right = len(arr) -1
    while left < right:
        width = right - left
        # height
        current_height = min(arr[left],arr[right])
        current_area = width * current_height
        # check for max level
        max_water = max(max_water,current_area)
        # change the state
        if arr[left] > arr[right]:
            right -= 1
        else:
            left += 1
    return max_water

"""
Valid Anagram
Standard: s1 = "listen", s2 = "silent" (Ans: True)

Different Lengths: s1 = "rat", s2 = "car" (Ans: False)

Case Sensitivity: s1 = "Anagram", s2 = "nagaram" (Ans: False — Unless you lowercase them)

With Spaces: s1 = "rail safety", s2 = "fairy tales" (Ans: True)

Empty Strings: s1 = "", s2 = "" (Ans: True)
"""

# my answer
def check_anagram(s1:str,s2:str):
    s1 = sorted("".join(s1.split(" ")))
    s2 = sorted("".join(s2.split(" ")))
    return s1 == s2

# perfect answer

from collections import Counter
def check_anagram(s1:str,s2:str):
    # clean the string and remove the spaces and make it lower
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    
    # quieck length check
    if len(s1) != len(s2):
        return False
        
    return Counter(s1) == Counter(s2)


"""
. First Non-repeating Character
Standard: "leetcode" (Ans: "l")

Middle Character: "loveleetcode" (Ans: "v")

All Repeating: "aabbcc" (Ans: None ya "")

Single Character: "z" (Ans: "z")

Case Sensitive: "AaBb" (Ans: "A")
"""

def first_non_repitative(s:str):
    r = []
    for i in s:
        if i not in r:
            r.append(i)
        else:
            r.remove(i)
    return r[0]


"""String Compression ("a3b2c1")
Standard: "aaabbc" (Ans: "a3b2c1")

No Repeats: "abc" (Ans: "a1b1c1")

Single Repeated: "aaaaaaaaaa" (Ans: "a10")

Large String: "aaabbbaaa" (Ans: "a3b3a3")

Empty String: "" (Ans: "")
"""
def string_comprehenssion(s:str)->str:
    res = ""
    count = 0
    temp = s[count]
    for i in range(len(s)):
        if s[i] == temp:
            count += 1
        else:
            res = res + f"{temp}{count}"
            temp = s[i]
            count = 1
    res = res + f"{temp}{count}" 
    return res

"""Group Anagrams
Standard: ["eat", "tea", "tan", "ate", "nat", "bat"]

Ans: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

No Anagrams: ["abc", "def", "ghi"] (Ans: [["abc"], ["def"], ["ghi"]])

Empty Elements: ["", ""] (Ans: [["", ""]])

Single Element: ["a"] (Ans: [["a"]])
"""



