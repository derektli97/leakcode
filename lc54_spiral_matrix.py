matrix = [[1,2,3],[4,5,6],[7,8,9]]

h = 0
v = 0

ROWS, COLS = len(matrix), len(matrix[0])

check_set = set()

res = []

            
        
for i in range(ROWS):
    for j in range(COLS):
        print(matrix[i][j])
        if j+1 == COLS:
            print('j+1', j+1)
            COLS -= 1

while ROWS or COLS:
    print('while start', matrix[v][h])
    for i in range(COLS):
        if h + 1 > COLS:
            COLS -= 1
    else:
        h +=1
    

# for i in range(COLS-1,-1,-1):
#     print('hi')
            
    












# while ROWS or COLS:
#     for i in range(ROWS-1):
        
        
#     if horizontal == COLS:
#         if [horizontal + 1, vertical] in check_set and [horizontal, vertical - 1] in check_set:
#             return res
#         else:
#             horizontal += 1
#             check_set.add([horizontal, vertical])
                    