x = []
rows = int(input('Enter the number of rows for the matrix: '))
columns = int(input('Enter the number of columns for the matrix: '))

for i in range(rows):
    a =[]
    for j in range(columns):
        a.append(int(input(f"Enter the value at the position ({i+1},{j+1}): ")))
    x.append(a)
print('The matrix you entered is:')
print(x)
print('The sum of respetive columns is:')
answer = 0
for i in range(len(x)):
    for j in range(len(x[0])):
        answer += x[j][i]
    print(answer,end=' ')
    answer = 0
            