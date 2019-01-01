class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        left = 0
        right = len(s) - 1
        dic = {}

        def maxsubpal(s, l, r):
            try:
                return dic[(l, r)]
            except:
                pass
            if l > r:
                dic[(l, r)] = (True, '')
                return (True, '')
            if l == r:
                dic[(l, r)] = (True, s[l])
                return (True, s[l])
            ans1 = maxsubpal(s, l + 1, r)
            ans2 = maxsubpal(s, l, r - 1)
            if s[l] == s[r]:
                temp = maxsubpal(s, l + 1, r - 1)
                if temp[0] == True:
                    ans3 = (True, s[l] + temp[1] + s[r])
                else:
                    ans3 = (False, temp[1])
                if len(ans3[1]) > max([len(ans1[1]), len(ans2[1])]):
                    dic[(l, r)] = ans3
                    return ans3
            to_return = (False, max([ans1, ans2], key=lambda i: len(i[1]))[1])
            dic[(l, r)] = to_return
            return to_return

        result = maxsubpal(s, left, right)[1]
        return result


a = "zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir"
print(Solution().longestPalindrome(a))