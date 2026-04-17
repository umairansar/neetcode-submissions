class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        alphabets = dict()
        for idx in range(26):
            letter = chr(ord('a') + idx)
            alphabets.update({letter:idx})
        print(alphabets)
        
        myAnagrams = dict()
        for word in strs:
            myKey = [0 for i in range(26)]
            for letter in word:
                myKey[alphabets[letter]] += 1
            myKeyStringified = ",".join(str(k) for k in myKey)

            if myKeyStringified in myAnagrams.keys():
                myAnagrams[myKeyStringified].append(word)
            else:
                myAnagrams[myKeyStringified] = [word]
        
        print(myAnagrams)
        
        res = []
        for k in myAnagrams.keys():
            res.append(myAnagrams[k])
        return res


        # mydict = dict()
        
        # for word in strs:
        
        #     isNewAnagram = True
        #     for ks in mydict.keys():
                
        #         # prevents subsets words from being identified as main word
        #         if len(word) != len(ks):
        #             continue

        #         isKeyMatched = True
        #         for letter in word:
        #             if letter not in ks:
        #                 isKeyMatched = False
        #                 break
                
        #         if isKeyMatched:
        #             isNewAnagram = False
        #             mydict[ks].append(word)
        #             break
            
        #     if isNewAnagram:
        #         mydict.update({word: [word]})

        # res = []    
        # for ks in mydict.keys():
        #     res.append(mydict[ks])
        # return res