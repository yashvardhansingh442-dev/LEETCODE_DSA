import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # max-heap simulation using negative values
        heap = [-s for s in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            first = -heapq.heappop(heap)   # largest stone
            second = -heapq.heappop(heap)  # second largest
            
            if first != second:
                heapq.heappush(heap, -(first - second))
        
        return -heap[0] if heap else 0
