class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr=[]
        for i in matrix:
            for j in i:
                arr.append(j)
        arr.sort()
        smallest= arr[k-1]
        return smallest