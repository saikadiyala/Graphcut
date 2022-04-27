import numpy as np
from nextBestPatch import *
from graphCut import *
from randomPatch import *
import matplotlib.pyplot as plot

def image_quilting(img,dimensions,patch_height,method):
    overlappingSize=patch_height//6
    patch_vertical,patch_horizontal =dimensions  
    count=0
    height=(patch_vertical*patch_height)-(patch_vertical-1)*overlappingSize
    width=(patch_horizontal*patch_height)-(patch_horizontal-1)*overlappingSize
    resultant=np.zeros((height,width,img.shape[2]))
    resultant_intermediate_1=np.zeros((height,width,img.shape[2]))
    resultant_intermediate_2=np.zeros((height,width,img.shape[2]))
    print("Dimensions of the output image are ",resultant.shape)
    for p in range(patch_vertical):
        for q in range(patch_horizontal):
            count=count+1
            j=p*(patch_height-overlappingSize)
            i=q*(patch_height-overlappingSize)    
            if p==0 and q==0:
                patch=randomPatch(img,patch_height)
                resultant_intermediate_1[j:j+patch_height, i:i+patch_height]=patch
                resultant_intermediate_2[j:j+patch_height, i:i+patch_height]=patch
            elif method=="graphCut":
                patch=nextBestPatch(img,patch_height,overlappingSize,resultant,j,i)
                patch,intermediate_1_patch,intermediate_2_patch=graphCut(patch,overlappingSize,resultant,j,i)
                resultant_intermediate_1[j:j+patch_height, i:i+patch_height]=intermediate_1_patch
                resultant_intermediate_2[j:j+patch_height, i:i+patch_height]=intermediate_2_patch                
            resultant[j:j+patch_height,i:i+patch_height]=patch
   
    return resultant,resultant_intermediate_1,resultant_intermediate_2



    










