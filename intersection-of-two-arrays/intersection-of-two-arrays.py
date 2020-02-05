
#Given two arrays, write a function to compute their intersection.



class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = []
        if len(nums1) > len(nums2):
            for i in nums2:
                if (i in nums1) and (i not in intersection):
                    intersection.append(i)
        else:
            for i in nums1:
                if (i in nums2) and (i not in intersection):
                    intersection.append(i)
        return intersection
                    