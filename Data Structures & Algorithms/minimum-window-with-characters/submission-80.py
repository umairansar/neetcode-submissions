class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        dict of counters t
        XXYZ => X:2, Y:1, Z:1
        s => "OUXZODYXXAZV"
        valids = []
        window = ""
        last_valid = false
        while s not traversed:
            move r to right and populate counter if in t {}
            if window is valid
                add window to valids
                set window to empty
                set last_valid true
            elif last_valid true or valids empty //window empty
                l += 1
                move l to left most valid character to right of current
                tracked by queue
                set last_valid false
        '''
        t_set = set(t)
        t_counter = dict()
        for c in t:
            t_counter[c] = 1 + t_counter.get(c, 0)
        
        l, r = 0, 0
        valids = []
        window = []
        window_counter = dict()
        last_iter_valid = False

        while r < len(s):
            print("(b)", l, r, s[r], window, window_counter)
            # Update window
            if s[r] in t_set or len(window) > 0:
                if len(window) > 0:
                    if window[-1][0] != r:
                        window.append((r, s[r]))
                        window_counter[s[r]] = 1 + window_counter.get(s[r], 0)
                else:
                    window.append((r, s[r]))
                    window_counter[s[r]] = 1 + window_counter.get(s[r], 0)
           
            # Move l after valid found
            if last_iter_valid and len(window) > 0:
                evicted_index = window[0][0]
                window_counter[s[evicted_index]] -= 1
                window = window[1:]
                r += 1
                if len(window) == 0:
                    continue
                while window[0][1] not in t_set:
                    window = window[1:]
                    if len(window) == 0:
                        break
                print("window => ", window)
                if len(window) != 0:
                    l = window[0][0]
                last_iter_valid = False

                if all(t_counter[k] <= window_counter.get(k, 0) for k in t_set):
                    valids.append("".join([k[1] for k in window]))
                    last_iter_valid = True
                    print("Valid => ", valids)
                    r -= 1

            # If valid window, save it, keep r as is
            elif all(t_counter[k] <= window_counter.get(k, 0) for k in t_set):
                valids.append("".join([k[1] for k in window]))
                last_iter_valid = True
                print("Valid => ", valids)
            
            # Move l before valid found
            elif len(valids) == 0 and len(window) != 0:
                l = window[0][0]
                r += 1
            else:
                r += 1

        print(valids)
        if len(valids) == 0:
            return "" 
        return min(valids, key=len)