class Solution:
    def longestPrefix(self, s: str) -> str:
        """
        try all prefixes with their corresponding suffixes
        n = len(s)
        n prefixes
        comparing prefix with suffix = n

        TC = O(n^2)

        s = "level"
        prefixes = ["l", "le", "lev", "leve"]
        suffixes = ["l", "el", "vel", "evel"]

        leve == evel
        lev == vel
        le == el
        l == l Found a match

        "ababab"
        a != b
        ab == ab
        aba != bab
        abab == abab
        ababa != babab

        optimization:
        hashing n^2 -> rolling hashing -> n

        input contains only lowercase english letters = 26 at max
        prefix = hash(s[0]) ^ 1 + hash(s[1]) ^ 2 ... hash(s[n]) ^ (n+1)
        suffix = hash(s[n]) ^ 1
        suffix *= 10 + hash(s[n-1]) ^ 1 an so on

        l = 7
        e = 3
        v = 5

        7 ^ 1 == 0 * 10 + 7 ^ 1 => 7 == 7
        7 + 3 ^ 2 == 7 * 10 + 3 ^ 2 => 16 != 79

        ababab
        a = 2
        b = 3

        1 2 3 4 5 1 2 3
        1 != 3
        12 != 23
        123 == 123
        """

        l = r = lhp = 0
        mod = 10**9 + 7
        for i in range(len(s)-1):
            l = (l * 128 + ord(s[i])) % mod
            r = (r + ord(s[-i-1]) * pow(128, i, mod)) % mod
            if l == r:
                lhp = i+1

        return s[:lhp]
