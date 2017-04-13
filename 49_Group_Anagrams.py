def groupAnagrams(strs):
    ana = {}
    for i in strs:
        s = ''.join(sorted(i))
        if s in ana:
            ana[s].append(i) 
        else:
            ana[s] = [i]
    
    print [ ana[x] for x in ana ]
            
        
        
        
        
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagrams(strs)
