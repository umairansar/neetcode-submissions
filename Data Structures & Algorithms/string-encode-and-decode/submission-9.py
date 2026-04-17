class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "Null"
        return chr(257).join(list(map(lambda x: str(x), strs)))

    def decode(self, s: str) -> List[str]:
        if s == "Null":
            return []
        return list(map(lambda x: x, s.split(chr(257))))
