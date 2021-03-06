import tensorflow as tf
import keras.backend as K
from tensorflow.keras.models import load_model,Model
from tensorflow.keras.layers import Input
from Models import c3d,c2d,mobilenetonly,c3d_lite,lstm,c3d_simple
from keras.preprocessing import image
import numpy as np
import os
import time
import statistics


mymodel = c3d_lite()
# path = os.path.join('6522')
X = np.empty((1,30,112,112,3), dtype = np.uint8)
# files = np.sort(np.array([os.path.splitext(filename)[0] for filename in os.listdir(path)]))
# files = files[:30]
# X[0] = np.array([image.img_to_array(image.load_img(path + "/" + str(f) + ".jpg", target_size=(112,112))) for f in files])

# X= np.random.rand(1,224,224,3)

# X= np.random.rand(1,30,1280)

timeList = []

timeList = []
for i in range(0,10):
	# X = np.random.rand(1,30,112,112,3)
	t0 = time.time()
	y = mymodel.predict(X)
	t1 = time.time()
	timeList.append(t1-t0)
	print("Inference time :", t1-t0)


print(statistics.mean(timeList[20:]))


# mymodel = c3d()
# path = os.path.join('6522')
# X = np.empty((1,30,112,112,3,), dtype = np.uint8)
# files = np.sort(np.array([os.path.splitext(filename)[0] for filename in os.listdir(path)]))
# files = files[:30]
# X[0] = np.array([image.img_to_array(image.load_img(path + "/" + str(f) + ".jpg", target_size=(112,112))) for f in files])
# timeList = []
# for i in range(0,10):
# 	t0 = time.time()
# 	y = mymodel.predict(X)
# 	t1 = time.time()
# 	timeList.append(t1-t0)
# 	print("Inference time :", t1-t0)

# print(statistics.mean(timeList[1:]))
