#ordenar el arreglo bidimensional de 3x3
arreglobidimensional = [
             [10, 35, 20],
             [45, 73.16],
             [34, 45,56],
           ]
for fila in range (len(arreglobidimensional)):
    for columna in range(len(arreglobidimensional[fila])):
        if columna == len(arreglobidimensional[fila])-1:
            print (arreglobidimensional[fila][columna])
        else:
            if arreglobidimensional[fila][columna] > arreglobidimensional[fila][columna+1]:
                                #[0]    [0] >                            [0]      [0]
                                    #10                                      35
                                #[0]    [1] >                            [0]      [2]
                                     #35                                       20
                varTemporal = arreglobidimensional[fila][columna]
                arreglobidimensional[fila][columna] = arreglobidimensional[fila][columna+1]
            #if arreglobidimensional[fila][columna+1]:
                arreglobidimensional [fila][columna +1] = varTemporal
                print (arreglobidimensional[fila][columna])
                print(arreglobidimensional[fila][columna]+1)
            else:
                print(arreglobidimensional[fila][columna])