def repeatedSubstringPattern(s):
        """
        :type s: str
        :rtype: bool
        """
        s_counts={}
        for letter in s:
            s_counts[letter] = s_counts.get(letter,0) +1
        values = list(s_counts.values())

        for value in values:
            if value != values[0]:
                return False
        return True
              


s='abcabcabcabcabc'
print(repeatedSubstringPattern(s))