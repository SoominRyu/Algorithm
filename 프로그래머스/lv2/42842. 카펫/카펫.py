
def solution(brown, yellow):
    answer = []
    
    # a : 가로  b: 세로
    ab = brown + yellow
    
    b1 = int((brown + 4)/2)   # a+b : 2a + 2(b-2) = brown
    
    # 세로 길이 <= 가로 길이 : 같은 길이부터 검사
    for b in range(int(b1/2),0,-1):
        if ab == (b * (b1-b)):
            answer = [b1-b, b]
            return answer
