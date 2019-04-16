class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        dic = {}
        start = 0
        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            if words1[i] in dic:
                if words2[i] in dic[words1[i]]:
                    continue
            found = 0
            for pair in pairs[start:]:
                if pair[0] in dic:
                    dic[pair[0]].append(pair[1])
                else:
                    dic[pair[0]] = [pair[1]]
                if pair[1] in dic:
                    dic[pair[1]].append(pair[0])
                else:
                    dic[pair[1]] = [pair[0]]
                if words1[i] == pair[0] and words2[i] == pair[1]:
                    start += 1
                    found = 1
                    break
                elif words1[i] == pair[1] and words2[i] == pair[0]:
                    start += 1
                    found = 1
                    break
                else:
                    start += 1
                    continue
            if found == 1:
                continue
            else:
                return False
        return True


words1 = ["a","very","delicious","meal"]
words2 = ["one","really","delicious","dinner"]
pairs = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]
print(Solution().areSentencesSimilar(words1, words2, pairs))
