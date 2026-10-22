class Solution:

    def encode(self, strs: List[str]) -> str:
        l = len(strs)
        s = ""
        for i in strs:
            s += "[*/"
            s += i
            s += "/*]"
        return s

    def decode(self, s: str) -> List[str]:
        l = len(s)
        arr = []
        word = ""
        ap = False
        i = 0
        while i < l:
            if s[i:i+3] == "/*]":
                ap = False
                arr.append(word)
                word = ""
                i += 2
            if ap:
                word += s[i] 
            if s[i:i+3] == "[*/":
                ap = True
                i += 2
            i += 1
        # for i in range(l):
        #     if ap:
        #         word += s[i] 
        #     if s[i:i+3] == "[*/":
        #         ap = True
        #     if s[i:i+3] == "/*]":
        #         ap = False
        #         arr.append(word)
        #         word = ""
        return arr





