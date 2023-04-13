R=int(input('enter number of rows: '))
C=int(input('enter number of column: '))
matrix=[]

print('enter number in new line','\n')

for i in range(R):
    a=[]
    for j in range(C):
        a.append(int(input('enter number: '))) 
    matrix.append(a)

# print(matrix)
for i in range(R):
    for j in range(C):
        if matrix[i][j] < 10:
            print('0'+str(matrix[i][j]),end=" ")
        else:
            print(matrix[i][j],end=' ')
    print()
