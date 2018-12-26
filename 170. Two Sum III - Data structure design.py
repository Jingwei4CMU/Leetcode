from collections import defaultdict
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.map[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i in list(self.map.keys()):
            if self.map[i] == 0:
                continue
            if i == value-i:
                if self.map[value-i] >= 2:
                    return True
            else:
                if self.map[value-i] >= 1:
                    return True
        return False

tar = TwoSum()
tar.add(1)
tar.add(-2)
tar.add(3)
tar.add(6)
print(tar.map)
print(tar.find(4))
print(tar.map)
print(tar.find(-1))
print(tar.map)
print(tar.find(9))
print(tar.map)
print(tar.find(10))
print(tar.map)
print(tar.find(5))
print(tar.map)
print(tar.find(0))
