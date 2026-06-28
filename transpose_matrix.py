x =[[2,3,5],
    [4,6,1],
    [7,8,0]]

answer = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        answer[i][j] = x[j][i]

for k in answer:
    print(k)
