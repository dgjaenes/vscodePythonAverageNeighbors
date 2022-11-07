

def createMatriz(n, m):
    matriz = []
    for i in range(n):
     a = [0]*m
     matriz.append(a)
    return matriz

def TransformMatriz(Matriz): 
 M2 = createMatriz(len(Matriz), len(Matriz[0]))
 for i_rows in range(0,len(Matriz)):
    for i_cols in range(len(Matriz[i_rows])):
        M2[i_rows][i_cols] = Prorccess_element(Matriz, i_rows, i_cols)
 return M2

def Prorccess_element(M, FIL, COL):
 
 L = [M[FIL][COL]]
 
 for i in range (FIL-1, FIL+2, 1):
        for j in range (COL-1, COL+2, 1):
            if i == FIL and j == COL:
                continue
            if i == len(M) or j == len(M[i]):
                break
            if i >= 0 and j >= 0 and (i == FIL or j == COL):
                L.append(M[i][j])
 
 return round((sum(L)/len(L)), 2)

def PrintMatriz(M):
  for i in range(len(M)):
     print(M[i])

M = [
     [4,5,0,0,0],
     [6,0,0,0,0],
     [0,-1,7,8,0],
     [0,0,9,0,0],
     [0,0,0,0,0],
     [0,0,2,0,0],
     [0,2,5,1,0],
    ]

print(" Matriz inicial:")
PrintMatriz(M)

print("Elemento essquina superior izquierda " + str(Prorccess_element(M, 0, 0)))
print("Elemento central " + str(Prorccess_element(M, 2, 2)))
print("Elemento borde inferior " + str(Prorccess_element(M, 6, 2)))

print(" Matriz transformada:")
M2 = TransformMatriz(M)

PrintMatriz(M2)