def canConstruct(ransomNote, magazine):
    print not collections.Counter(ransomNote) - collections.Counter(magazine)
import collections  
canConstruct("fffbfg", "effjfggbffjdgbjjhhdegh")



def canConstruct(ransomNote, magazine):
    for i in set(ransomNote):
        if ransomNote.count(i) > magazine.count(i):
            return False
    return True  
