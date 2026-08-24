class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            hashmap = {}

            for digit in row:
                if digit != '.':
                    hashmap[digit] = hashmap.get(digit, 0) + 1

            for value in hashmap.values():
                if value > 1:
                    return False

        for col in range(9):
            hashmap = {}

            for row in range(9):
                digit = board[row][col]

                if digit != '.':
                    hashmap[digit] = hashmap.get(digit, 0) + 1

            for value in hashmap.values():
                if value > 1:
                    return False

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                hashmap = {}

                for i in range(3):
                    for j in range(3):
                        digit = board[row + i][col + j]

                        if digit != '.':
                            hashmap[digit] = hashmap.get(digit, 0) + 1

                for value in hashmap.values():
                    if value > 1:
                        return False

        return True