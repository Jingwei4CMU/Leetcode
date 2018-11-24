class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # Runtime: 36 ms, faster than 99.78% of Python3 online submissions for Most Common Word.
        paragraph = paragraph.replace(',',' ').replace('.',' ').replace('!',' ')\
            .replace('?',' ').replace('\'',' ').replace(';',' ').lower()
        allwords = paragraph.split(' ')
        result = ''
        rcount = 0
        for word in set(allwords):
            if word in banned or word == '':
                continue
            tempcount = allwords.count(word)
            if tempcount > rcount:
                result = word
                rcount = tempcount
        return result








print(Solution().mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.",banned = ["hit"]))