# Leetcode
不好好刷题就找不到工作  
!!!Submission detail 可以看到不同Run time 的代码sample!!!  
An **in-place** algorithm is an algorithm which transforms input using no auxiliary data structure.  


##11.22.2018 Thursday Thanksgiving Holiday  
####1 two sum:

`if i not in dict`

Look for index in dict, not the content 

####7 Reverse Integer
`string` can be used as `list`

####13 Roman to Integer
`list[<start>:<stop>:<step>]`

####14 Longest Common Prefix
string slice  
`ss[6:11]`
 
####20. Valid Parentheses
For Python:  
`list.append` is from the last  
`list.pop` is pop from the first  
`list.insert(index,item)`    
`top_element = stack.pop() if stack else '#'`  
This code do not need to check if stack is empty !!!  

##11.23.2018 Friday
####21. Merge Two Sorted Lists
!!! Need to remember the input sometimes is not friendly.!!!
Use recursive to solve some shit

####27. Remove Element  
Two pointers, one is fast, the other is slow  

####35. Search Insert Position
Binary search:  
if the middle point has been checked, the pointer can be 
set lower or higher than the middle.  

####141. Linked List Cycle  
Object can be used as key of dictionary  
Approach 2: Two Pointers  
Imagine two runners if there is cycle.  
Good point is the space complicity can be O(1)  

####53. Maximum Subarray  
Need to do again  

####121. Best Time to Buy and Sell Stock  
Get the min and max in sequence in one loop.  

####771. Jewels and Stones  
`Jset = set(J)`  
`return sum([i in Jset for i in S])`
`i in Jset` is boolean, and for i in S is condition of i

####482. License Key Formatting  
`string.upper()`  
`join` is used to list, do not use string as input  

####283. Move Zeroes  
`list.append(list.pop())`  

####88. Merge Sorted Array  
`sorted(list)`  
`sorted(x, reverse = True) `



