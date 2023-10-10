def solution(prices):
    answer = []
        
    for i in range(len(prices)-1):
        count = 1
        for j in range(i+1, len(prices)-1):
            if (prices[i] <= prices[j]):
                count += 1
            else:
                break
        answer.append(count)
    answer.append(0)
        
    return answer
