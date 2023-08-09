# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol    Value
# I           1
# V           5
# X           10
# L           50
# C           100
# D           500
# M           1000

#  for example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply
# X + II.The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right.However, the numeral
# for four is not IIII.Instead, the number four is written as IV.Because the one is before the five we subtract it making four.The same principle applies to the number nine, which is written as IX.There are six instances where subtraction
# is used:
# I can be placed before V(5) and X(10) to make 4 and 9.
# X can be placed before L(50) and C(100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
#
# Example
# 1:
#
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example
# 2:
#
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V = 5, III = 3.

# Example 3:
#
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Constraints:
#
# 1 <= s.length <= 15
# s contains only the characters('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range[1, 3999].

# solution:

roman_no=input("Enter the roman number:")
roman_no=roman_no.upper()
roman_no=roman_no+" "
flag=0
integral_no=0
i=0
while((i<len(roman_no)-1)):
    if roman_no[i]=="I" and roman_no[i+1]=="V":
        integral_no+=4
        i+=2
    elif roman_no[i]=="I" and roman_no[i+1]=="X":
        integral_no+=9
        i+=2
    elif roman_no[i] == "X" and roman_no[i + 1] == "L":
        integral_no += 40
        i += 2
    elif roman_no[i] == "X" and roman_no[i + 1] == "C":
        integral_no+=90
        i+=2
    elif roman_no[i] == "C" and roman_no[i + 1] == "D":
        integral_no += 400
        i += 2
    elif roman_no[i] == "C" and roman_no[i + 1] == "M":
        integral_no+=900
        i+=2
    elif roman_no[i]=="I":
        integral_no+=1
        i+=1
    elif roman_no[i] == "V":
        integral_no += 5
        i += 1
    elif roman_no[i] == "X":
        integral_no += 10
        i += 1
    elif roman_no[i] == "L":
        integral_no += 50
        i += 1
    elif roman_no[i] == "C":
        integral_no += 100
        i += 1
    elif roman_no[i] == "D":
        integral_no += 500
        i += 1
    elif roman_no[i] == "M":
        integral_no += 1000
        i += 1
    else:
        print("please enter valid roman number")
        flag=1
        break
if flag==0:
    print(integral_no)

#question 2:

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower", "flow", "flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog", "racecar", "car"]
# Output: ""
# Explanation: There is no ommon prefix among the  input strings.
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# solution
def longestcommonprefix(listofstrings):
    if len(listofstrings[0]) < len(listofstrings[1]):
        lengthofsmallstr = len(listofstrings[0])
    else:
        lengthofsmallstr = len(listofstrings[1])
    k = 0
    while (k < lengthofsmallstr):
        if listofstrings[0][k] == listofstrings[1][k]:
            prefixlist.append(listofstrings[0][k])
            k += 1
        else:
            break

    prefix = "".join(prefixlist)

    if prefix != "":
        i = 2
        while (i < lengthofstringlist):
            if listofstrings[i].startswith(prefix):
                i += 1
            else:
                prefixlist.pop()
                prefix = "".join(prefixlist)
                if prefix == "":
                    print("No common prefix ")
                    break
        print(prefix)
    else:
        print("No common prefix")


lengthofstringlist=int(input("Enter the number of strings :"))
i=0
listofstrings=[]
prefixlist=[]
while i<lengthofstringlist:
    listofstrings.append(input(f"Enter string {i+1} :").lower())
    i+=1
if len(listofstrings)>1:
   longestcommonprefix(listofstrings)
else:
    print(listofstrings[0])


# question3
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input is    valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Every close bracket has a corresponding open bracket of the same type.
# Open brackets must be closed in the correct order.
#Example 1:
#
#
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# solution:
def isvalidstring(opening,closing):
    j=0
    while(j<len(opening)):
        if opening[j]=="{" and closing[-(j+1)]=="}":
            j+=1
        elif  opening[j]=="[" and closing[-(j+1)]=="]":
             j+=1
        elif  opening[j]=="(" and closing[-(j+1)]==")":
            j+=1
        else:
            return False
    else:
        return True
string=input("Enter string:")
opening=[]
closing=[]
flag=False
for char in string:
  if char not in "{[()]}":
      flag=True
      break
if flag!=True:
    i=0

    while i<len(string):
         while(i<len(string)):
             if string[i] in "{([":
                 opening.append(string[i])
                 i+=1
             else:
                 break
         while(i<len(string)):
             if string[i] in ")}]":
                closing.append(string[i])
                i+=1
             else:
                break
         if len(opening)!=len(closing):
            flag=True
            break
         else:
           returnvalue= isvalidstring(opening,closing)
           opening.clear()
           closing.clear()
           if returnvalue!=True:
               flag=True
               break
if flag==False:
    print(True)
else:
    print(False)



# Question 4:
#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
 # Return k.

 # Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

# solution:
def removeduplicates(numbers):
    j=0
    while(j<len(numbers)):
        num=numbers[j]
        count=numbers.count(num)
        j+=1
        while(count!=1):
            numbers.remove(num)
            count-=1
    numbers.sort()
    return len(numbers)

length=int(input("Enter the number of elements in array:"))
i=0
numbers=[]
while(i<length):
    numbers.append(int(input(f"Enter number {i+1}:")))
    i+=1
required_length=removeduplicates(numbers)
print(required_length,numbers)

# question 5:
# You are given a 0-indexed array words consisting of distinct strings.
# The string words[i] can be paired with the string words[j] if:
# The string words[i] is equal to the reversed string of words[j].
# 0 <= i < j < words.length.
# Return the maximum number of pairs that can be formed from the array words.
# Note that each string can belong in at most one pair.

# Example 1:
# Input: words = ["cd","ac","dc","ca","zz"]
# Output: 2
# Explanation: In this example, we can form 2 pair of strings in the following way:
# - We pair the 0th string with the 2nd string, as the reversed string of word[0] is "dc" and is equal to words[2].
# - We pair the 1st string with the 3rd string, as the reversed string of word[1] is "ca" and is equal to words[3].
# It can be proven that 2 is the maximum number of pairs that can be formed.

# Example 2:
# Input: words = ["ab","ba","cc"]
# Output: 1
# Explanation: In this example, we can form 1 pair of strings in the following way:
# - We pair the 0th string with the 1st string, as the reversed string of words[1] is "ab" and is equal to words[0].
# It can be proven that 1 is the maximum number of pairs that can be formed.

# Example 3:
# Input: words = ["aa","ab"]
# Output: 0
# Explanation: In this example, we are unable to form any pair of strings.

# Constraints:
# 1 <= words.length <= 50
# words[i].length == 2
# words consists of distinct strings.
# words[i] contains only lowercase English letters.

# solution

length=int(input("Enter the number of words in array:"))
i=0
word_list=[]
while(i<length):
    word_list.append(input(f"Enter {i+1} word:").lower())
    i+=1
i=0
j=1
flag=0
count=0
if length!=1:
  while(True):
    while(j<len(word_list)):
        if word_list[i]!=word_list[j][::-1]:
            j+=1

        else:
            count+=1
            word_list.pop(j)
            word_list.pop(i)
            j=1
            if len(word_list)==0 or len(word_list)==1:
             flag=1
             break
    else:
        word_list.pop(i)
        j=1
        if len(word_list)==1:
            flag=1
            break
    if flag==1:
        break
print(count)



