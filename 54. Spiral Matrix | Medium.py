#https://leetcode.com/problems/spiral-matrix/description/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        if len(matrix) == 1:
            return [q for q in matrix[0]]
        if len(matrix[0]) == 1: # for stupid edge cases
            for k in matrix:
                answer.append(k[0])
            return answer
        cycle = 0 #0 means top, right is 1, bottom is 2, left is three
        for x in range(len(matrix)*3):
            if cycle == 0:
                if len(matrix) == 0:
                    break
                for z in matrix[0]:
                    answer.append(z)
                matrix.pop(0)
                cycle = 1
                continue
            if cycle == 1:
                if len(matrix) == 0:
                    break
                for o in matrix:
                    if len(o) == 0:
                        return answer
                    answer.append(o[-1])
                    o.pop(-1)
                cycle = 2
                continue
            if cycle == 2:
                if len(matrix) == 0:
                    break
                for b in reversed(matrix[-1]):
                    answer.append(b)
                matrix.pop(-1)
                cycle = 3
                continue
            if cycle == 3:
                temp = []
                if len(matrix) == 0:
                    break
                for o in matrix:
                    if len(o) == 0:
                        return answer
                    temp.append(o[0])
                    o.pop(0)
                for h in reversed(temp):
                    answer.append(h)
                cycle = 0
                continue
        return answer
