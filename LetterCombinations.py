class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        lookup = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        lst = []
        def helper(tracker, i):
            if not digits[i:]:
                lst.append(tracker)
            else:
                for j in lookup[digits[i]]:
                    helper(tracker+j, i+1)
        helper('', 0)
        return lst
