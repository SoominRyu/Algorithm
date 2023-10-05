def solution(s):
    
    slist = list(s)
    sum = 0
    for s in slist:
        if s == '(':
            sum += 1
        elif s == ')':
            sum -= 1
        
        if sum < 0:
            break
    
    if sum != 0:
        return False
    else:
        return True
    