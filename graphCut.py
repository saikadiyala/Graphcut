from pickle import TRUE
import numpy as np
import cv2 as cv
from overlappedPatch import *
from minCut import *
from graphConstruction import *



def graphCut(patch, overlappingSize, resultant, j, i):
    patch = patch.copy()
    intermediate_1_patch = patch.copy()
    intermediate_2_patch = patch.copy()  
    dj, di, _ = patch.shape
    if i > 0:
        patch1=patch[:,:overlappingSize]
        patch2=resultant[j:j+dj, i:i+overlappingSize]    
        commonRegion=graphConstruction(patch1, patch2)      
        left,right,visited=minCut(commonRegion)  
        resultant_patch,region,over_region = overlappedPatch(visited, patch1, patch2)
        for p in range(0,patch1.shape[0]):
            for q in range(0,patch1.shape[1]):
                patch[p][q]=resultant_patch[p][q]
                intermediate_1_patch[p][q]=over_region[p][q]
                intermediate_2_patch[p][q]=region[p][q]            
    if j > 0:
        patch1=patch[:overlappingSize,:]
        patch2=resultant[j:j+overlappingSize, i:i+di]   
        patch1=cv.rotate(patch1,cv.cv2.ROTATE_90_CLOCKWISE)
        patch2=cv.rotate(patch2,cv.cv2.ROTATE_90_CLOCKWISE)
        commonRegion=graphConstruction(patch1, patch2)      
        leftImageSet=set()
        rightImageSet=set()
        boolArray=[]
        for i in range(0,len(patch1)):
            tempBoolArr=[]
            for j in range(0,len(patch1[0])):
                tempBoolArr.append(False)
            boolArray.append(tempBoolArr)
        left,right,visited=minCut(commonRegion)
        count=0
        for i in range(0,len(left)):
                count=left[i]
                ctr = 0
                if(left[i]!=right[i-1]):
                    x=(count%25)-1
                    while(x<=left[i-1]):
                        leftImageSet.add(count)
                        boolArray[x][ctr] = True
                        x+=25
                        ctr+=1
                    while(ctr<=overlappingSize):
                        rightImageSet.add(x)
                        x+=25
        
        for i in range(len(patch2)):

            for j in range(len(patch2[0])):

                if(boolArray[i][j] == TRUE):
                    patch2[i][j] = patch[i][j]    
        resultant_patch,region,over_region=overlappedPatch(visited, patch1, patch2)  
        resultant_patch = cv.rotate(resultant_patch, cv.cv2.ROTATE_90_COUNTERCLOCKWISE)
        region = cv.rotate(region, cv.cv2.ROTATE_90_COUNTERCLOCKWISE)
        over_region = cv.rotate(over_region, cv.cv2.ROTATE_90_COUNTERCLOCKWISE)     
        for p in range(0,patch1.shape[1]):
            for q in range(0,patch2.shape[0]):
                patch[p][q] = resultant_patch[p][q]
                intermediate_1_patch[p][q] = over_region[p][q]
                intermediate_2_patch[p][q] = region[p][q]

    return patch,intermediate_1_patch,intermediate_2_patch


