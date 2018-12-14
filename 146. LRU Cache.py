from collections import OrderedDict
class LRUCache:
    # # should work, but error on website
    # def __init__(self, capacity):
    #     """
    #     :type capacity: int
    #     """
    #     self.capacity = capacity
    #     self.cache_dict = {}
    #
    #
    # def get(self, key):
    #     """
    #     :type key: int
    #     :rtype: int
    #     """
    #     try:
    #         temp_value = self.cache_dict[key]
    #         del self.cache_dict[key]
    #         self.cache_dict[key] = temp_value
    #         return temp_value
    #     except:
    #         return -1
    #
    # def put(self, key, value):
    #     """
    #     :type key: int
    #     :type value: int
    #     :rtype: void
    #     """
    #     keys = list(self.cache_dict.keys())
    #     if len(keys) == self.capacity:
    #         del self.cache_dict[keys[0]]
    #     self.cache_dict[key] = value


    # Runtime: 108 ms, faster than 99.24% of Python3 online submissions for LRU Cache.
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache_dict = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            to_return = self.cache_dict[key]
            self.cache_dict.move_to_end(key)
            return to_return
        except:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.cache_dict[key] = value
        self.cache_dict.move_to_end(key)
        if len(self.cache_dict)>self.capacity:
            self.cache_dict.popitem(last=False)


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))