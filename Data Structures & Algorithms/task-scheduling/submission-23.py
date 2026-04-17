class Solution: # 1st Iteration - Works
    def leastInterval(self, tasks: List[str], n: int) -> int:

        def heapify(taskFreq):
            freqTask = [(-t[1], t[0]) for t in taskFreq.items()]
            heapq.heapify(freqTask)
            return freqTask

        counter = {}
        for task in tasks:
            counter[task] = counter.get(task, 0) + 1

        m = len(tasks)
        selector = heapify(counter)
        queue = []
        processed = 0
        step = 0
        while processed < m:
            if queue: # consume one idle step from queue
                freq, task = queue[0]
                queue = queue[1:]
                if freq:
                    heapq.heappush(selector, (freq, task))

            if selector: # process in the same step
                task = heapq.heappop(selector)[1]
                counter[task] -= 1
                if counter[task] > 0:
                    idleCount = n if not queue else max(0, n - len(queue))
                    queue.extend([(None, "idle")] * idleCount)
                    queue.append((-counter[task], task))
                processed += 1
            
            step += 1
        
        return step
                
