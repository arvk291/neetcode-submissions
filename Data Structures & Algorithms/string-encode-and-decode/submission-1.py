class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs):
            return '___'.join(strs)
        else:
            return "empty"


    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        decoded_string_list = []
        for word in s.split('___'):
            decoded_string_list.append(word)
        return decoded_string_list
