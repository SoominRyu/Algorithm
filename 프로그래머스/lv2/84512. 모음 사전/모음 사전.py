from itertools import product 

def solution(word):
    alpha = [ 'A', 'E', 'I', 'O', 'U']
    w = list()
    
    # 모든 경우의 수, 중복O , 순서O
    for j in range(1,6):
        for i in product(alpha,repeat=j):
            w.append(list(i))
    w.sort() # 정렬
    
    answer = w.index(list(word)) + 1
    return answer