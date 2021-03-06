"ONE WAY TO SOLVE IT" 

import collections 
class Solution(object):
    def intersection(self, nums1, nums2):
        a = list(set(nums1)) + list(set(nums2))
        b = collections.Counter(a)
        arr = []
        for i in range(len(b)): 
            if b.values()[i] == 2: 
                arr.append(b.keys()[i])
        return arr
    
    
    
" ANOTHER WAY" 
class Solution(object):
    def intersection(self, nums1, nums2):
        arr = [] 
        for i in set(nums1): 
            if i in set(nums2): 
                arr.append(i)
        return arr 
