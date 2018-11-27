def classifiers(x, N, M): #input NxM image(2d aray [N][M]) x, output length 6 feature array
    # 1)
    Density = sum(x)/(N*M)
    # 2)
    DOFS += x[i][j] ^ x[j][i] for i in range(N) for j in range(M)
    DOFS /= (N*M)
    # 3,4,5,6)
    BW = [[0]*M]*N #initialize a new NxM array
    BW[i][j] = int(x[i][j]<=128) for i in range(N) for j in range(M) #thresholding operation
    # 3,4)
    Cols = []
    # 5,6)
    Rows = []
    # 3,4)
    for i in range(N): #find number of changes between 0 and 1, for columns
        p = BW[i][0]
        count = 0
        for j in range(M): #Column Major
            if(p != BW[i][j]):
                count += 1
                p =BW[i][j]
        Cols.append(count)
    # 5,6)
    for j in range(M): #find number of changes between 0 and 1, for rows
        p = BW[0][j]
        count = 0
        for i in range(N): #Row Major
            if(p != BW[i][j]):
                count += 1
                p =BW[i][j]
        Rows.append(count)
    # 3)
    maxInterHoriz = max(Cols)
    # 4)
    aveInterHoriz = sum(Cols)/len(Cols)
    # 5)
    maxInterVert = max(Rows)
    # 6)
    aveInterVert = sum(Rows)/len(Rows)
    return [Density, DOFS, maxInterHoriz, aveInterHoriz, maxInterVert, aveInterVert]
    #order: [Density, Degree/Measure of Symettry, maximum horizontal intersections, average horizntal intersections, maximum vertical intersections, average vertical intersections]

    
    
