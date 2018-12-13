class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        # Runtime: 96 ms, faster than 18.96% of Python3 online submissions for Subdomain Visit Count.
        times_list = []
        domain_list = []
        for domain in cpdomains:
            times = int(domain.split(' ')[0])
            address = domain.split(' ')[1][::-1]
            # print(times)
            # print(address)
            tempindex_list = [i for i, e in enumerate(address) if e == '.']
            while tempindex_list:
                # print(address)
                # print(tempindex_list)
                tempdomain = address[:tempindex_list.pop(0)]
                try:
                    thisindex = domain_list.index(tempdomain)
                    times_list[thisindex] += times
                except:
                    domain_list.append(tempdomain)
                    times_list.append(times)
            try:
                thisindex = domain_list.index(address)
                times_list[thisindex] += times
            except:
                domain_list.append(address)
                times_list.append(times)

        # print(times_list)
        # print(domain_list)
        result = []
        for i in range(len(domain_list)):
            result.append(str(times_list[i])+' '+domain_list[i][::-1])
        return result








print(Solution().subdomainVisits(["900 google.mail.com",
                                  "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))