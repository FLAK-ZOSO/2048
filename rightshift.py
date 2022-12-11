matrix: list[list[int]] = [
    [2, 2, 4, 2],
    [4, 0, 0, 0],
    [0, 4, 4, 0],
    [2, 2, 0, 0]
]

for row in matrix:
    while (True):
        if (row[3] == 0 and row[2] == 0 and row[1] == 0 and row[0] == 0): # Se tutti gli elementi sono vuoti...
            break
        elif (row[3] == 0 and row[2] == 0 and row[1] == 0): # Se gli ultimi tre elementi sono vuoti...
            row[3] = row[0]
            row[0] = 0
        elif (row[3] == 0 and row[2] == 0): # Se gli ultimi due elementi sono vuoti...
            row[3] = row[1]
            row[2] = row[0]
            row[1] = 0
            row[0] = 0
        elif (row[3] == 0): # Se l'ultimo elemento è vuoto...
            # ... sposta tutto a destra
            row[3] = row[2]
            row[2] = row[1]
            row[1] = row[0]
            row[0] = 0

        if (row[3] == row[2] or row[2] == row[1] or row[1] == row[0]): # Se ci sono due elementi uguali...
            for i in {3, 2, 1}:
                if (row[i] == row[i-1]):
                    row[i] *= 2
                    row[i-1] = 0
                    break
        else:
            break

print(matrix)