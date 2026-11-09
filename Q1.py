def solution(A,K):
    
    if len(A) == 0:
        return A
        
    for i in range(K):
        last = A[-1]
        A = A[:-1]
        A = [last] + A
        
    return A
    