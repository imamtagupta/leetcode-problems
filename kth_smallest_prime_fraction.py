
######################################
# 786. K-th Smallest Prime Fraction   #
######################################

# leetcode link: https://leetcode.com/problems/k-th-smallest-prime-fraction/

from heapq import heapify, heappop, heappush
from typing import List
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        # Create a min-heap of tuples, with each tuple containing the fraction,
        # the index of the numerator, and the index of the denominator.
        min_heap = [(arr[0] / arr[j], 0, j) for j in range(1, len(arr))]
      
        # Convert the list into a heap in-place.
        heapify(min_heap)
      
        # Pop the smallest fraction from the heap 'k - 1' times,
        # since we need to find the kth smallest fraction.
        for _ in range(k - 1):
            # Pop the smallest element (fraction) from the heap.
            smallest_fraction, i, j = heappop(min_heap)
          
            # If we can move the numerator to the right in the array to get
            # another fraction with the same denominator, push that fraction to the heap.
            if i + 1 < j:
                new_numerator_index = i + 1
                new_fraction = (arr[new_numerator_index] / arr[j], new_numerator_index, j)
                heappush(min_heap, new_fraction)
      
        # After popping k-1 elements, the smallest fraction in the min-heap
        # is the kth smallest fraction. Return this fraction as [numerator, denominator].
        smallest_fraction, numerator_index, denominator_index = min_heap[0]
        return [arr[numerator_index], arr[denominator_index]]