class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
     def searchRange(self, A, B):
        start = 0
        end = len(A)
        mid = (start + end) //2
        startFound = False
        finalStart = -1
        finalEnd = -1
        while (start <= mid <= end):
            if (A[mid] == B):
                    if (mid==0) or (A[mid-1] != B):
                        startFound = True
                        finalStart = mid
                        break
                    end = mid-1
                    mid = (start + end) //2
            elif A[mid] < B:
                start = mid + 1
                mid = (start + end) //2
            else:
                end = mid - 1
                mid = (start + end ) // 2
        
        endFound = False
        start = finalStart
        end = len(A)
        mid = (start + end ) // 2
        while (start <= mid <= end):
            if (A[mid] == B):
                    if (mid==(len(A)-1)) or (A[mid+1] != B):
                        endFound = True
                        finalEnd = mid
                        break
                    start = mid+1
                    mid = (start + end) //2
            elif A[mid] < B:
                start = mid + 1
                mid = (start + end) //2
            else:
                end = mid - 1
                mid = (start + end ) // 2

        if (startFound == False):
            return [-1,-1]
        
        return[finalStart, finalEnd]