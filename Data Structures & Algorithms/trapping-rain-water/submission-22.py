class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) == 0 or len(height) == 1:
            return 0

        l_peaks = []
        l_max = 0
        for i, v in enumerate(height):
            if v > l_max:
                l_max = v
                l_peaks.append([i, v])

        r_peaks = []
        r_max = 0
        for i, v in enumerate(reversed(height)):
            orig_i = len(height) - 1 - i
            if v > r_max:
                r_max = v
                r_peaks.append([orig_i, v])
        
        print("l_peaks")
        print(l_peaks)
        print("r_peaks")
        print(r_peaks)
        
        res = 0
        l_peak = l_peaks[-1]
        r_peak = r_peaks[-1]
        l = l_peak[0]
        print("l_peak" + str(l_peak))
        r = r_peak[0]
        print("r_peak" + str(r_peak))
        if l == r:
            if len(r_peaks) >= 2:
                r_peak = r_peaks[-2]
                r = r_peak[0]
                print("r_peak" + str(r_peak))
                r_peaks = r_peaks[:-1]
            elif len(l_peaks) >= 2:
                l_peak = l_peaks[-2]
                l = l_peak[0]
                print("l_peak" + str(l_peak))
                l_peaks = l_peaks[:-1]
            else:
                return 0

        fill = min(l_peak[1], r_peak[1])
        print("fill: " + str(fill))
        for i in range(l+1, r):
            print(fill - height[i])
            res += (fill - height[i])
        print("res: " + str(res))

        print(l_peaks)
        for i in range(0, len(l_peaks)):
            if i + 1 < len(l_peaks):
                fill = min(l_peaks[i][1], l_peaks[i+1][1])
                print("fill-l: " + str(fill))
                if l_peaks[i][0] + 1 != l_peaks[i+1][0]:
                    for k in range(l_peaks[i][0] + 1, l_peaks[i+1][0]):
                        res += (fill - height[k])
        print("res 1: " + str(res))

        print(r_peaks)
        for i in range(0, len(r_peaks)):
            if i + 1 < len(r_peaks):
                fill = min(r_peaks[i][1], r_peaks[i+1][1])
                print("fill-r: " + str(fill))
                if r_peaks[i][0] - 1 != r_peaks[i+1][0]:
                    for k in range(r_peaks[i][0] - 1, r_peaks[i+1][0], -1):
                        res += (fill - height[k])
                    # res += (fill - height[i])
        print("res 2: " + str(res))

        return res
        # left, right = 0, len(l_peak) - 1
        # while left < right:
        #     left_height = l_peak[left][1]
        #     right_height = l_peak[right][1]
        #     fill = min(left_height, right_height)
        #     res = []

        #     if left_height < right_height:
        #         left += 1
        #     else 
        #         right -= 1

        # for l in range(len(l_peak)):
        #     if l + 1 < len(l_peak):
        #         if l_peak[l][0] + 1 != l_peak[l][0]:

