from collections import defaultdict
import string
class Solution(object):
    # # width first work but too much time
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
    #     if endWord not in wordList:
    #         return 0
    #     visit_dict = defaultdict(int)
    #     visit_dict[beginWord] = 1
    #     visit_list = [(beginWord, 1)]
    #     while visit_list:
    #         word_now, step_now = visit_list.pop(0)
    #         try:
    #             wordList.remove(word_now)
    #         except:
    #             pass
    #         for to_visit in wordList:
    #             if visit_dict[to_visit] == 0 and self.dist(word_now,to_visit) == 1:
    #                 if to_visit == endWord:
    #                     return step_now + 1
    #                 visit_dict[to_visit] = 1
    #                 visit_list.append((to_visit,step_now+1))
    #
    #     return 0
    # def dist(self,a,b):
    #     to_return = 0
    #     for i in range(len(a)):
    #         if a[i] != b[i]:
    #             to_return += 1
    #     return to_return


    # # depth first search wrong answer
    #
    # def ladderLength(self, beginWord, endWord, wordList):
    #     if endWord not in wordList:
    #         return 0
    #     wordList.insert(0,beginWord)
    #     visit_dict = defaultdict(int)
    #     visit_dict[beginWord] = 1
    #     step = 1
    #     return self.search(0,wordList,visit_dict,endWord,step)
    #
    # def search(self,index, wordList,visit_dict,endWord,step):
    #     thisword = wordList[index]
    #     # print('this word:',thisword)
    #     if thisword == endWord:
    #         return step
    #     visit_dict[thisword] = 1
    #     for nextword_index in range(len(wordList)):
    #         if visit_dict[wordList[nextword_index]] == 0 and self.dist(thisword, wordList[nextword_index]) == 1:
    #             tempresult = self.search(nextword_index,wordList,visit_dict,endWord,step+1)
    #             if tempresult > 0 :
    #                 return tempresult
    #     return 0
    #
    #
    # def dist(self,a,b):
    #     to_return = 0
    #     for i in range(len(a)):
    #         if a[i] != b[i]:
    #             to_return += 1
    #     return to_return

        if endWord not in wordList:
            return 0
        head = set()
        tail = set()

        head.add(beginWord)
        tail.add(endWord)
        wordList = set(wordList)
        if beginWord in wordList:
            wordList.remove(beginWord)
        wordList.remove(endWord)
        c = 1
        while head:
            if len(head) > len(tail):
                head, tail = tail, head
            tmp = set()
            while head:
                curw = head.pop()
                for i in range(len(curw)):
                    left = curw[:i]
                    right = curw[i + 1:]
                    for mutate in string.ascii_lowercase:
                        newWord = left + mutate + right
                        if newWord in tail:
                            return c + 1
                        if newWord in wordList:
                            wordList.remove(newWord)
                            tmp.add(newWord)

            c += 1
            head = tmp
        return 0





print(Solution().ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))