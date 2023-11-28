# import json
# import cv2
# import numpy as np
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

# def main():
#     # 读取images文件和labels文件
#     with open('images.txt', 'r') as f:
#         images = f.readlines()
#     with open('labels.txt', 'r') as f:
#         labels = f.readlines()
    
#     # 将图像路径和标签信息整理成二维数组
#     data = np.array([[line.split(' ')[0], line.split(' ')[1]] for line in open('labels.txt', 'r').readlines()]
#                    + [[line.split(' ')[0], line.split(' ')[2]] for line in open('labels2.txt', 'r').readlines()])
#     X = data[:, 0]
#     y = data[:, 1]
    
#     # 读取图像数据和对应的标签数据
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
#     # 定义模型
#     model = Sequential()
#     model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
#     model.add(MaxPooling2D((2, 2)))
#     model.add(Conv2D(64, (3, 3), activation='relu'))
#     model.add(MaxPooling2D((2, 2)))
#     model.add(Flatten())
#     model.add(Dense(64, activation='relu'))
#     model.add(Dense(1, activation='sigmoid'))
    
#     # 编译模型
#     model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
#     # 训练模型
#     model.fit(np.array(X_train), np.array(y_train), epochs=10, batch_size=32, validation_data=(np.array(X_test), np.array(y_test)))
    
#     # 保存模型
#     model.save('image_classification_model.h5')

# if __name__ == '__main__':
#     main()



#前面要把文件名修改 

# %cd /home/aistudio/work/
# # 从github上下载PaddleDetection
# # !git clone https://github.com/PaddlePaddle/PaddleDetection.git -b develop

# # 使用提前准备好的PaddleDetection代码包
# !wget https://bj.bcebos.com/v1/paddledet/code/PaddleDetection-release-2.5.zip
# !unzip -q PaddleDetection-release-2.5.zip
# !mv PaddleDetection-release-2.5 PaddleDetection

# %cd ~
# %cd work/PaddleDetection
# # 安装相关依赖
# !pip install -r requirements.txt

# # 编译安装paddledet
# !python setup.py install

# <?xml version="1.0" encoding="UTF-8"?>
# <annotation>
#   <filename>1.jpg</filename>
#   <object_num>1</object_num>
#   <size>
#     <width>320</width>
#     <height>240</height>
#   </size>
#   <object>
#     <name>bump</name>
#     <difficult>0</difficult>
#     <bndbox>
#       <xmin>107</xmin>
#       <ymin>65</ymin>
#       <xmax>246</xmax>
#       <ymax>125</ymax>
#     </bndbox>
#   </object>
# </annotation>