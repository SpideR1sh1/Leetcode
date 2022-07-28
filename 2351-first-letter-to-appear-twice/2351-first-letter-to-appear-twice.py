class Solution:
    def repeatedCharacter(self, s: str) -> str:
        map = {}
        
        for i, char in enumerate(s):
            map[char]  = map.get(char, 0) + 1
            
            if map[char] == 2:
                return char
            