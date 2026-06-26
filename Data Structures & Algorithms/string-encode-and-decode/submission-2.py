class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + "\x1f" 
        return res

    def decode(self, s: str) -> List[str]:
        return s.split("\x1f")[:-1]


