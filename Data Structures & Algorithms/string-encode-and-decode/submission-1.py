class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = "*"
        for string in strs:
            encode += ",".join([str(ord(st)) for st in string]) + "*"
        return encode
    def decode(self, s: str) -> List[str]:
        decode =[]
        if len(s) == 1:
          return []
        s = s[1:-1]
        for string in s.split("*"):
            decoded_string = ""
            for st in string.split(","):
                if len(st) != 0:
                    decoded_string += chr(int(st))
            decode.append(decoded_string)
        return decode