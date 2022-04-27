import numpy as np

def nextBestPatch(img,patch_height,overlappingSize,resultant,j,i):
    h, w, _=img.shape
    err=np.zeros((h-patch_height,w-patch_height))
    for p in range(h - patch_height):
        for q in range(w - patch_height):
            patch = img[p:p+patch_height, q:q+patch_height]
            e = error_fun(patch, patch_height, overlappingSize, resultant, q, p)
            err[p, q] = e
    p, q = np.unravel_index(np.argmin(err), err.shape)
    return img[p:p+patch_height, q:q+patch_height]
def error_fun(patch, patch_height, overlappingSize, resultant, j, i):
    error = 0
    if i > 0:
        leftPatch = patch[:, :overlappingSize] - resultant[j:j+patch_height, i:i+overlappingSize]
        error =error+np.sum(leftPatch**2)
    if j > 0:
        upperPatch = patch[:overlappingSize, :] - resultant[j:j+overlappingSize, i:i+patch_height]
        error =error+np.sum(upperPatch**2)
    if i > 0 and j > 0:
        leftUpperPatch = patch[:overlappingSize, :overlappingSize] - resultant[j:j+overlappingSize, i:i+overlappingSize]
        error =error-np.sum(leftUpperPatch**2)
    return error






