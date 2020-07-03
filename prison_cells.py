class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if cells[0] == 1 or cells[-1] == 1:
            N = (N-1) % 14 + 1
        else:
            N = N % 14

        for n in range(N):
            orig = cells[0]
            cells[0] = 0
            for i in range(1, len(cells)-1):
                if orig == cells[i+1]:
                    val = 1
                else:
                    val = 0
                orig = cells[i]
                cells[i] = val
            cells[-1] = 0

        return cells
