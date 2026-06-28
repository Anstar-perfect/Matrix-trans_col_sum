x = [[12,0,9],
     [4,7,54],
     [24,6,8]]

answer =0

for i in range(len(x)):
    for j in range(len(x[0])):
        answer += x[j][i]
    print(answer,end=' ')
    answer=0
