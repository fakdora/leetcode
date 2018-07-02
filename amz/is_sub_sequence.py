class Solution(object):

    # subsequence is not substring
    # ace is a subsequence of 'abcde'
    def isSubsequence(self, s, t):
        for c in s:
            i = t.find(c)
            if i == -1:
                return False
            else:
                t = t[i+1:]
        return True
