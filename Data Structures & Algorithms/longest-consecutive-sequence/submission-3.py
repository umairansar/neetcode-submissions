class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        mydict = dict()
        for num in nums:

            keys = mydict.keys()
            if num in keys:
                continue
            
            #True means it can be a starting point
            mydict[num] = [True, None]
            if (num-1) in keys:
                mydict[num-1][1] = num
                mydict[num][0] = False
            if (num+1) in keys:
                mydict[num][1] = num+1
                mydict[num+1][0] = False

        print(mydict)

        results = []
        for (k, (is_start, v)) in mydict.items():
            print(k, is_start)
            if not is_start:
                continue
            
            next_num = v
            res = [k]
            while next_num is not None:
            # for i in range(1):
                # print("temp", temp)
                res.append(next_num)
                next_num = mydict[next_num][1]
            # print("next_num", next_num)
            # next_num/ = mydict[v[1]]
            print("res", res)
            results.append(res)
        
        sizes = list(map(lambda x: len(x), results)) + [0]
        print(sizes)
        return max(sizes)


        # myDict = dict()
        # for num in nums:
            
        #     keys = myDict.keys()
        #     if num  in keys:
        #         continue
            
        #     myDict[num] = [num]
        #     print("Insert", num)
        #     if (num+1) in keys:
        #         myDict[num].extend(  myDict[num+1] )
        #     if (num-1) in keys:
        #         myDict[num-1].extend(  myDict[num])
        #         sync = num-1
        #         while(sync - 1 in keys):
        #             print(sync, keys)
        #             myDict[sync-1].append( num )
        #             sync -= 1
        #     print(myDict)
            
        # print(myDict)

        # res = 0
        # for (k, v) in myDict.items():
        #     if res < len(v):
        #         res = len(v)
        # return res