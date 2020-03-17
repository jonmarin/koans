
from typing import List


def write_spiral( arr: List[int] ):
    print("Before", arr)
    dim = len( arr )

    step = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = 0
    curr = (0,0)
    for i in range( dim ** 2):
        print(curr)
        arr[curr[0]][curr[1]] = i+1
        nxt = (curr[0] + step[direction][0], curr[1] + step[direction][1])
        if nxt[0] >= dim or nxt[1] >= dim or arr[nxt[0]][nxt[1]] != 0:
            direction = (direction + 1) % 4
            nxt = (curr[0] + step[direction][0], curr[1] + step[direction][1])

        curr = nxt

    print("After", arr)


num = 3
ret = write_spiral( [ [0 for i in range(num)] for j in range(num)] )

