import numpy as np


def overlappedPatch(visited, patch1, patch2):
    map2Original = {}
    resultant_patch = np.zeros(shape=(patch1.shape[0],patch1.shape[1],3))
    count = 1
    for p in range(len(patch1[0])):
        for q in range(len(patch1)):
            map2Original[count] = (q,p)
            count += 1           
    region = np.zeros_like(resultant_patch)
    over_region = np.zeros_like(resultant_patch)   
    for i in range(1,len(visited)-1):
        row = map2Original[i][0]
        col = map2Original[i][1]       
        if visited[i]:
            resultant_patch[row][col] = np.array(patch2[row][col])
            region[row][col] = np.array([255,0,0])
            over_region[row][col] = np.array([255,0,0])
        else:
            resultant_patch[row][col] = np.array(patch2[row][col])
            region[row][col] = np.array([255,0,0])
            over_region[row][col] = np.array([255,0,0])           
    return resultant_patch,region,over_region

    