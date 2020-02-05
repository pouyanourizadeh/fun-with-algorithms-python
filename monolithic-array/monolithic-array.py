#An array is monotonic if it is either monotone increasing or monotone decreasing.
#
#An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
#
#Return true if and only if the given array A is monotonic.

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if (len(A) == 1) or (len(A) == 2):
            return True
        is_increasing = False
        if A[0] < A[-1]:
            is_increasing = True
        
        if is_increasing:
            for i in range(0,len(A)):
                try:
                    if A[i] > A[i+1]:
                        return False
                except:
                    continue
        else:
            for i in range(0,len(A)):
                try:
                    if A[i] < A[i+1]:
                        return False
                except:
                    continue
                    
        return True