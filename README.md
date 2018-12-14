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
####929. Unique Email Addresses  
`dic.keys()` to get the keys in a dictionary.  
`len(dic.keys())` get the number of keys in a dictionary  
`str.split('@')` will return a list, all items are with out `'@'` , and
there can be empty strings in teh list.  
####67. Add Binary  
`int('string',2)` convert to binary int  
####70. Climbing Stairs  
Climb stairs problem is a Fibonacci problem  
####204. Count Primes
Find the prime number, m*m.  
Need to do again.
####811. Subdomain Visit Count
`from collections import defaultdict`
`counts = defaultdict(int)`
This dict will not throw error if input wrong key,
and the initial value will be zero.
We can directly add number to it.
`counts['d'] += 1`  
`counts.items()` will return both key and value  
`count, domain = cpdomain.split(" ")` keep in mind  
####716. Max Stack
`from heapq import *`  
`heappush(heap,item)`  
`heappop(heap)`  
`temp = set()`  
`temp.add(sth)`  
####146. LRU Cache
`from collections import OrderedDict`
This dict will have a very useful function 
`dict = OrderedDict()`  
`dict.move_to_end(key)`will remember the order of keys
`dict.popitem(last=False/True)` will pop the last or first item






