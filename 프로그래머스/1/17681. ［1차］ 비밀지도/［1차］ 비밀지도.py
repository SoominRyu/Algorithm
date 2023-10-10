def nbox(n, arr, box):       
    for i in range(n):
        a1 = arr[i]
        for j in range(n-len(a1)):
            if(n-len(a1)-1) >= 0:
                a1.insert(0,0)
        box.append(a1)
    
    return box


def solution(n, arr1, arr2):
    box = []
    arr_bin1 = [list(map(int,format(i, 'b'))) for i in arr1]
    arr_bin2 = [list(map(int,format(i, 'b'))) for i in arr2]
    
    arr_box1 = nbox(n, arr_bin1, list())
    arr_box2 = nbox(n, arr_bin2, list())

    for b in range(n):
        box1, box2 = arr_box1[b], arr_box2[b]
        secret = ''
        for b1, b2 in zip(box1, box2):
            if b1+b2 == 0:
                secret += ' '
            else:
                secret += '#'
                
        box.append(secret)

    return box