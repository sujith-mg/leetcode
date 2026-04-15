import heapq

class MedianFinder(object):

    def __init__(self):
        self.small = []  # max heap (invert values)
        self.large = []  # min heap

    def addNum(self, num):
        # Step 1: Add to max heap
        heapq.heappush(self.small, -num)
        
        # Step 2: Balance: move top of small → large
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Step 3: Maintain size property
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0