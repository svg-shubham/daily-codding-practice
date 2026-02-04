# Reverse a string without using built-in functions/slicing.
s = "shubham"
def rev_string(s):
  a = ""
  for i in range(len(s)-1,-1,-1):
    a += s[i]

  return a

# print(rev_string(s))

a = "aba"
# def check_palindrome(s):
#   return s == s[::-1] # this will creash when data is in 1 gb and more that time it will be crashed

def is_pallindrome(s):
  s = "".join(char.lower() for char in s if char.isalnum())
  left = 0
  right = len(s) -1
  while left < right:
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1
  return True
# print(is_pallindrome("A man, a plan, a canal: Panama"))

# Q : - Find the second largest number in a list in a single pass.
s = [10,9,12,11,14,3]
# def sec_highest(s):
#   return sorted(s)[-2] using this on normal level it will solve the problem but memory may cause that break when it will more in memory

def finding_second_highest(s):
    if len(s) < 2:
        return None
    first = second = float('-inf') 
    for i in s:
        if i > first:
            second = first
            first = i
        elif i > second and i != first:
            second = i
            
    return second if second != float('-inf') else None

# print(finding_second_highest([10, 20, 4, 45, 99]))
# print(finding_second_highest([10, 10, 10]))
#Q4 Valid Parentheses
def valid_parentheses(s):
    para = {"}": "{", "]": "[", ")": "("}
    stack = []
    for i in s:
        if i not in para:
            stack.append(i)
        else:
            if not stack or stack.pop() != para[i]:
                return False
    return len(stack) == 0
        

# to get min number using o(1) time complecity 
# i can try min() methed for that but because of that small calculations are done gratelly but when there is huge data at that time i have to do with that beacuse of that min() method get o(n) time complexity

class MinStack():
  def __init__(self):
    self.stack = []
    self.min_stack = []

  def push(self,value:int):
     self.stack.append(value)
     if not self.min_stack or value <= self.min_stack[-1]:
        self.min_stack.append(value)

  def pop(self):
    if self.stack[-1] == self.min_stack[-1]:
        self.min_stack.pop()
    self.stack.pop()

  def top(self) -> int:
        return self.stack[-1]

  def getMin(self) -> int:
      return self.min_stack[-1]
  
# 2. AB TEST KARO (Isse run karke output dekho)
# obj = MinStack()

# print("--- Step 1: Push 10, 20, 5 ---")
# obj.push(10)
# obj.push(20)
# obj.push(5)
# print(f"Current Min: {obj.getMin()}") # Output: 5

# print("\n--- Step 2: Push 2 ---")
# obj.push(2)
# print(f"Current Min: {obj.getMin()}") # Output: 2

# print("\n--- Step 3: Pop (2 gaya) ---")
# obj.pop()
# print(f"Current Min: {obj.getMin()}") # Output: 5 (Wapas 5 ho gaya!)

# print("\n--- Step 4: Top element kya hai? ---")
# print(f"Top: {obj.top()}")

#Question 6: Evaluate Reverse Polish Notation (RPN)
# RPN kya hota hai? Normal math mein hum likhte hain 2 + 1. RPN mein ise likhte hain ["2", "1", "+"]. Iska matlab hai ki pehle numbers aayenge, phir operator (+, -, *, /).

s = ["2", "1", "+", "3", "*"]
def RPN(s):
  stack = []
  for i in s:
    if i in "+-*/":
      v1 = int(stack.pop())
      v2 = int(stack.pop())
      if i == "+":
          stack.append(v2 + v1)
      elif i == "-":
          stack.append(v2 - v1)
      elif i == "*":
          stack.append(v2 * v1)
      elif i == "/":
          stack.append(int(v2 / v1))
    else:
      stack.append(int(i))
          
  return stack[0]

# print(RPN(s))
"""
Binary Search: Ek sorted array mein se ek number dhoondna hai. Lekin shart ye hai ki loop $O(n)$ nahi, balki $O(\log n)$ hona chahiye (Yaani har baar array ko aadha karte jao).
"""

def binary_search(arr, target):
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid 
    elif arr[mid] < target:
        low = mid + 1
        
    else:
        high = mid - 1
          
  return -1

def calculate_square_root(number,tolarance = 0.001):
   if number < 0:
      return None
   if number == 0:
      return 0
   guess = number / 2.0

   while abs(guess * guess - number) >= tolarance:
      guess = (guess + number / guess)/ 2.0
   return guess

# number = 25
# sqrt_result = calculate_square_root(number)
# print(f"The square root of {number} is approximately: {sqrt_result}")

# number = 2
# sqrt_result = calculate_square_root(number)
# print(f"The square root of {number} is approximately: {sqrt_result}")