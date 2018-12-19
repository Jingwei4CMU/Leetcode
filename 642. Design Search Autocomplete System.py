class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        


    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """







sentences = ["i love you", "island", "ironman", "i love leetcode"]
times = [5, 3, 2, 2]

obj = AutocompleteSystem(sentences, times)
c = "i"
param_1 = obj.input(c)
print(param_1)