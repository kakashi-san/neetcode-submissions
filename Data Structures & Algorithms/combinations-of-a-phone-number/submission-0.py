class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def rec(i):
            if i == len(digits):
                return [[]]

            curr_letters = digit_to_letters[digits[i]]
            next_set = rec(i + 1)

            ret = []
            for letter in curr_letters:
                for nex in next_set:
                    ret.append([letter] + nex)

            return ret

        combos = rec(0)
        return ["".join(combo) for combo in combos]