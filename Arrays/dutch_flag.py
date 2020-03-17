from typing import List


RED, WHITE, BLUE = range(3)

def dutch_flag_partition( pivot_index: int, A: List[int] )  -> None:
    pivot = A[pivot_index]
    #first pass, group elements smaller than pivot
    for i in range( len(A) ):
        #look for smaller element
        for j in range( i+1, len(A)):
            if A[j] < pivot:
                    A[i], A[j] = A[j], A[i]
                    break

    for i in reversed( range(len(A))):
        #look for larger element.
        for j in reversed( range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break



if __name__ == "__main__":
    A = [4, 8, 9, 7, 2, 2]
    pivot_index = 3

    print(*A)
    dutch_flag_partition( pivot_index, A)
    print(*A)
