class Solution(object):
    def shiftingLetters(self, s, shifts):
        res = ""
        temp = 0
        for i in range(len(shifts) -1, -1, -1):
            shift = temp + shifts[i]
            temp = shift
            if shift > 26:
                shift = shift % 26
            res = self.getShiftedChar(ord(s[i]), shift) + res
        return res

    def getShiftedChar(self, char, shift):
        asc = char
        asc += shift
        while asc > 122:
            diff = asc - 122
            asc = 96 + diff

        char = chr(asc)
        return char
