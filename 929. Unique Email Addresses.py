class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        # Runtime: 48 ms, faster than 96.04% of Python3 online submissions for Unique Email Addresses.
        adic = {}
        for email in emails:
            index_plus = email.index('+')
            index_at = email.index('@')
            final_email = email[:index_plus].replace('.','') + email[index_at:]
            if adic.get(final_email) == None:
                adic[final_email] = 0
        return len(adic.keys())








print(Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))