class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxs = []
        l = 0
        r = len(heights) - 1
        while l != r:
            slots = r - l
            l_height = heights[l]
            r_height = heights[r]
            min_height = min(l_height, r_height)
            maxs.append(min_height * slots)
            if l_height < r_height:
                l += 1
            else:
                r -= 1
        return max(maxs)

        