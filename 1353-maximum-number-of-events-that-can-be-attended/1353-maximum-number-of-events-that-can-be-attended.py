class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()

        started = []
        count, i = 0, 0
        today = events[0][0]
        while i<n:
            while i<n and events[i][0] == today:
                heappush(started, events[i][1])
                i += 1

            heappop(started)
            count += 1
            today += 1

            while started and started[0]<today: heappop(started)
            if i<n and not started: today = events[i][0]

        while started:
            if heappop(started)>=today:
                today += 1
                count += 1

        return count