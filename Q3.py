def solution(A):
    total = sum(A)
    left = 0
    minimum = abs(A[0] - (total - A[0]))
    for i in range(len(A)-1):
        left = left + A[i]
        right =total - left
        diff = abs(left - right)
        if diff < minimum:
            minimum = diff
    return minimum