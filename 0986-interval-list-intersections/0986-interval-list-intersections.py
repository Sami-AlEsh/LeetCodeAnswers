class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []
        
        while i < len(firstList) and j < len(secondList):
            a_in_b = firstList[i][0] >= secondList[j][0] and firstList[i][0] <= secondList[j][1]
            b_in_a = secondList[j][0] >= firstList[i][0] and secondList[j][0] <= firstList[i][1]
            
            if a_in_b or b_in_a:
                result.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return result