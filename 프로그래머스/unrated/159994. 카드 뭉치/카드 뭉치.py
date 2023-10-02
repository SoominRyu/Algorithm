# 기존 풀이
# def solution(cards1, cards2, goal):
#     answer = ''
#     n1 = 0
#     n2 = 0
#     for i in goal:
#         if i == cards1[n1]:
#             if n1 < len(cards1)-1:
#                 n1 += 1
#         elif i == cards2[n2]:
#             if n2 < len(cards2)-1:
#                 n2 += 1
#         else:
#             answer = 'No'
#             break
#         # print(n1, n2)
#         answer = 'Yes'
#     return answer


# pop 사용
def solution(cards1, cards2, goal):
    for i in goal:
        if len(cards1) > 0 and i == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and i == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
        # print(cards1, cards2, i)
    return "Yes"
