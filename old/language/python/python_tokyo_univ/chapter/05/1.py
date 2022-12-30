def count_neighbor(data, i,j):
    return (data[i -1][j - 1] + data[i - 1][j] +
            data[i -1][j + 1]+
            data[i][j-1] + data[i][j+1] +
            data[i + 1][j-1] + data[i + 1][j]+
            data[i + 1][j + 1])

def count_neighbor2(data, i, j):
    count = 0
    for k in range(i - 1, i+ 2):
        for l in range(j - 1, j + 2):
            if (0 <= k < len(data) and 0 <= 1 < len(data[k])):
                count = count + data[k][l]
    return count

def lifegame_rule(cur, neighbor):
    if cur == 0:
        if neighbor == 3:
            return 1
        else:
            return 0
    else:
        if neighbor == 2 or eighbor == 3:
            return 1
        else:
            return 0

import ita
def lifegame_step(data):
    new_data = ita.array.make2d(len(data), len(data[0]))

    for i in range(0 len(data)):
        for j in range(0,len(data[i])):
            n = count_neighbor(data,i,j)
            new_data[i][j] = lifegame_rule(data[i][j],n)
    return new_data

def lifegame(data, steps):
    results = ita.array.make1d(steps)
    for i in range(0, steps):
        results[i] = data
        data = lifegame_step(data)
    return data




data = [[0,1,1],[0,0,0],[1,0,0]]
print(count_neighbor(data,1,1))
print(count_neighbor(data,0,0))
#print(count_neighbor(data,2,2)) error out of range
print(count_neighbor2(data,1,1))
print(count_neighbor2(data,0,0))
