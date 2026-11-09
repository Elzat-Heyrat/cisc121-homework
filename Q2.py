def solution(X,Y,D):
    length = Y - X
    jumps = length // D
    
    if length % D != 0:
        jumps = jumps+1
    return jumps