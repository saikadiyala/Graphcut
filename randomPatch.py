import numpy as np

def randomPatch(img, patch_height):
    #np.random.seed(1111)
    height, width, _ = img.shape
    p = np.random.randint(height - patch_height)
    q = np.random.randint(width - patch_height)
    patch = img[p:p+patch_height, q:q+patch_height]
    return patch
    