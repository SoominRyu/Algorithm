def solution(cards1, cards2, goal):
    answer = ''
    n = 0
    for i in goal:
        if i == cards1[0] and len(cards1)>1:
            del cards1[0]
        elif i == cards2[0] and len(cards2)>1:
            del cards2[0]
        else:
            answer = 'No'
            break
        print(cards1, cards2)
        answer = 'Yes'
    return answer

def solution(cards1, cards2, goal):
    answer = ''
    n1 = 0
    n2 = 0
    for i in goal:
        if i == cards1[n1]:
            if n1 < len(cards1)-1:
                n1 += 1
        elif i == cards2[n2]:
            if n2 < len(cards2)-1:
                n2 += 1
        else:
            answer = 'No'
            break
        # print(n1, n2)
        answer = 'Yes'
    return answer