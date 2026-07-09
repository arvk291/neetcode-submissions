class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op_dict = dict()
        for item in strs:
            item_sorted = "".join(sorted(item))
            if item_sorted not in op_dict.keys():
                op_dict[item_sorted] = [item]
            else:
                op_dict[item_sorted].append(item)
        return list(op_dict.values())