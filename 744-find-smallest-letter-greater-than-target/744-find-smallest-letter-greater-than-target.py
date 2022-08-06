class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target == 'z':
            target = chr(ord('a') - 1)
            
        start = 0
        end = len(letters) - 1
        smallest = None
        while start <= end:
            mid = (start+end) // 2
            if ord(target) < ord(letters[mid]):
                smallest = letters[mid]
                end = mid - 1
            elif ord(target) >= ord(letters[mid]):
                start = mid + 1
        
        return smallest if smallest else letters[start % len(letters)]