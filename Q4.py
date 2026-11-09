def solution(X,A):
    leaves = [False] * (X +1) #create list to record which positions already have leaves
    count = 0
    for i in range (len(A)):
        position = A[i]
        
        if leaves[position] == False: #check if that is the first time have leaves on that position 
            leaves[position] = True 
            count = count +1
            
        if count == X:
            return i
    return -1