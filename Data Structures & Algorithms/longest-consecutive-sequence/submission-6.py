class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        starters = set()
        mapping = {}

        for num in nums:
            if num in mapping:
                continue
            mapping[num] = None
            starters.add(num)
            if num-1 in mapping:
                mapping[num-1] = num
                starters.discard(num)               
            if num+1 in mapping:
                mapping[num] = num+1
                starters.discard(num+1)
        
        print(starters, mapping)
        counters = []
        for starter in starters:
            counter = 1
            key = starter
            while mapping.get(key) != None:
                print(key)
                counter += 1
                key = mapping[key]
            print("counter ", counter)
            counters.append(counter)

        return max(counters)

        # O(n) only possible without sorting
        # Then only way left is to hash and
        # travers the dict to find LCS 
