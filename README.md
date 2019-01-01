# Leetcode
不好好刷题就找不到工作  
!!!Submission detail 可以看到不同Run time 的代码sample!!!  
An **in-place** algorithm is an algorithm which transforms input using no auxiliary data structure.  

###Holiday plan
Easy 113 1219-1223 25/D
Medium 100 1224-1228 20/D
amazon 100 1229-0103 15/D

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
####138. Copy List with Random Pointer
copy objects, should not change the original
one. If we can not change the attributes of 
object, we can just double the objects.  
####23. Merge k Sorted Lists
`heapq` is really a good tool.
It can be used to sort several lists.

## 2018.12.19  
Today to do easy * 18  
####198. House Robber  
dynamic programming!  
get the formula  
####122. Best Time to Buy and Sell Stock II  
Done  
####339. Nested List Weight Sum  
Done  
####415. Add Strings  
Done  
####438. Find All Anagrams in a String
Anagram  
`ord('a')`  
`chr(97)`  
convert a key to a list and compare with others.
####125. Valid Palindrome
`import string`,`string.ascii_lowercase`,`string.punctuation`.  
punctuation does not include space.
`string.ascii_letters`
####709. To Lower Case
Done
####234. Palindrome Linked List
Done
####136. Single Number  
`^` XOR  
####170. Two Sum III - Data structure design
defaultdict will remember key even if just look it up  
####190. Reverse Bits  
`zfill`   `str.zfill(32)` fill the left side with zeros  
`bin(n)` convert n to binary
####235. Lowest Common Ancestor of a Binary Search Tree
binary search tree the root is between left and right 
####867. Transpose Matrix  
`[0]*n` will create n 0s with the same address, once on is changed, the others will change.
`B = [1,2,3]` and `A = B` will make A the same address with B.  
we can use deepcopy to create a new list with different address  
`import copy` and then `A = copy.deepcopy(B)`  
####532. K-diff Pairs in an Array  
`set()&set()` will return the intersection of two sets.  
`from collections import Counters` then `a = Counters(d)` will return a counter
just like a dictionary.  
`Counters.items`, `Counters.values`   
####246. Strobogrammatic Number
`import operator`  `map(operator.add,a,a[::-1])` then `set`
set can be compared by `<=`
####56. Merge Intervals  
`sth = sorted(sth, key=lambda i:i.start)` here, sth can be the list of list, or 
list of objects.
####322. Coin Change  
`float('inf')` and `float('-inf')` will not change with adding or subtracting  
####236. Lowest Common Ancestor of a Binary Tree
for tree, sometime we can cut the useless tree nodes, but before doing that, we need
some operations.
####264. Ugly Number II
`ugly = sorted(2**a * 3**b * 5**c for a in range(32) for b in range(20) for c in range(14))`
####698. Partition to K Equal Sum Subsets
`any()` return True if at least one if True.






