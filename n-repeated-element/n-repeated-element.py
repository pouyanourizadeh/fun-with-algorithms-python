#In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

#Return the element repeated N times.


class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        array_stats = {}
        for i in A:
            try:
                array_stats[i] += 1
            except:
                array_stats[i] = 1
        for key,value in array_stats.items():
            if (len(A) == value * 2):
                return key