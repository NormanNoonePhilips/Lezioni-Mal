
def longest(palindromi):
    s = ''
    for x in palindromi:
        if (len(x) > len(s)):
            s = x
    return s
    
def longestPalindrome(s: str):
    palindromi = []
    for i in range(len(s) - 1):
        if (s[i] == s[i + 1]):
            sTemp = ''
            sTemp += s[i]
            j = 1
            while ((i - j) > 0 and (i + 1 + j) < len(s)
                   and s[i - j] == s[i + 1 + j]):
                sTemp += s[i - j]
                j += 1
            palindromi.append(sTemp[::-1] + sTemp)
        if ((i + 2) < len(s) and s[i] == s[i + 2]):
            sTemp = ''
            sTemp += s[i]
            j = 1
            while ((i - j) >= 0 and (i + 2 + j) < len(s)
                   and s[i - j] == s[i + 2 + j]):
                sTemp += s[i + 2 + j]
                j += 1
            palindromi.append(sTemp[::-1] + s[i + 1] + sTemp)
    return longest(palindromi)

print(longestPalindrome("baaaaabaa"))