rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
x = []
for i in range(rows):
    a = []
    for j in range(columns):
        a.append(int(input(f'Enter the element at position ({i+1},{j+1}): ')))
    x.append(a)
print('The matrix you entered:')
print(x)
print('The sum of respective rows is:')
answer = 0
for i in range(len(x)):
    for j in range(len(x[0])):
        answer += x[i][j]
    print(answer,end=' ')
    answer = 0


