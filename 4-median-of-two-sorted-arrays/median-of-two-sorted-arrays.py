class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Simple approach: merge both sorted arrays, then pick the middle
        merged = []
        i, j = 0, 0

        # Merge like we do in merge sort
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        # Add leftover elements
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        n = len(merged)
        mid = n // 2

        if n % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2
        else:
            return merged[mid]