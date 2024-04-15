#https://leetcode.com/problems/integer-to-roman/description/
class Solution:
    def intToRoman(self, num: int) -> str:
        spotzero = ['I','II','III','IV','V','VI','VII','VIII','IX']
        spotone = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        spottwo = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        big = ['M', 'MM', 'MMM']
        roman = [spotzero, spotone ,spottwo ,big]
        answer = []
        for spot, digit in enumerate(reversed(str(num))):
            if digit == '0':
                continue
            answer.append((roman[spot])[int(digit)-1])
        return ''.join(reversed(answer))
