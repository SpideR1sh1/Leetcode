class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        encoded = ''

        for s in strs:
            encoded += s.replace('/', '//') + '/:'
        
        return encoded
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        decoded = []

        curr = ""
        i = 0
        while i < len(s):
            if s[i:i+2] == '/:':
                decoded.append(curr)
                curr = ""
                i += 2
            elif s[i:i+2] == '//':
                curr += '/'

                i += 2
            else:
                curr += s[i]
                i += 1
        
        
        return decoded

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))