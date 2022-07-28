class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        
        for char in s:
            map[char] = map.get(char, 0) + 1
        
        for i, char in enumerate(s):
            if map[char] == 1:
                return i
        return -1
            