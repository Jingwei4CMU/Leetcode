import bisect
class Solution:
    def maxEnvelopes(self, envelopes):
        tails = []
        for w, h in sorted(envelopes, key = lambda x: (x[0], -x[1])):
            i = bisect.bisect_left(tails, h)
            if i == len(tails): tails.append(h)
            else: tails[i] = h
        return len(tails)

a = [[1,4],[1,2],[1,7],[1,5]]
print(Solution().maxEnvelopes(a))