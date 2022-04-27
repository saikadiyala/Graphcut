import cv2 as cv
import matplotlib.pyplot as plot
import numpy as np
from quilting import *


img=cv.imread('forest.jpg')
print("Dimensions are  ",img.shape)
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
plot.imshow(img)
plot.show()
a=img-np.min(img)
b=np.max(img)-np.min(img)
img=a/b
quilted_image,intermdiate_image_1,intermdiate_image_2=image_quilting(img,[6,6],25,"graphCut")
plot.imshow(quilted_image)
plot.show()
plot.imshow(intermdiate_image_1)
plot.show()
plot.imshow(intermdiate_image_2)
plot.show()


    











