class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            add = str(len(s)) + "#"
            encoded += (add + s)

        return encoded

    def decode(self, s: str) -> List[str]:

        decoded = ""
        i = 0
        decoded = []
        print(s)

        while i < len(s):
            curr_num = ""

            while i < len(s) and s[i].isdigit() and s[i] != "#":
                curr_num += s[i]
                i += 1
            if s[i] == "#" and len(s) > 0:
                curr_word = s[i+1: i + int(curr_num) + 1]
                decoded.append(curr_word)
                i = i + int(curr_num) + 1
        
        return decoded




