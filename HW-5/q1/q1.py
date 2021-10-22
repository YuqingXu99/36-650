
def transpose_matrix(X):
    result = []
    for i in range(len(X[0])):
        list1 = []
        for j in range(len(X)):
            list1.append(X[j][i])
        #print(list1)
        result.append(list1)
    return result

X = [[10,8],
 [2 ,4],
 [1 ,7]]
transpose_matrix(X)