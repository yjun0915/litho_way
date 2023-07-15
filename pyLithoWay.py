import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

hWeight, vWeight = 0, 0
w = 1

def load_image(image_path):
    image = Image.open(image_path)
    image = image.convert("RGB")
    return image

def image_to_array(image):
    width, height = image.size
    array = np.array(image.getdata()).reshape(height, width, 3)
    return array
    
def array_to_grayscale_array(array):
    grayscale_array = np.dot(array[...,:3], [0.2989, 0.5870, 0.1140])
    return grayscale_array
    
def array_to_REDscale_array(array):
    REDscale_array = array[...,0]
    return REDscale_array
    
def array_to_GREENscale_array(array):
    REDscale_array = array[...,1]
    return REDscale_array
    
def array_to_BLUEscale_array(array):
    REDscale_array = array[...,2]
    return REDscale_array

def convolut(array):
    matrix = np.array([
        [hWeight+vWeight, vWeight, -hWeight+vWeight], 
        [hWeight, 0, -hWeight], 
        [hWeight-vWeight, -vWeight, -hWeight-vWeight]
    ])
    
    new_array = []
    
    ax, ay = np.shape(array)
    mx, my = np.shape(matrix)
    
    for i in range(ax - mx + 1):
        for j in range(ay - my + 1):
            value = (array[i:i+mx, j:j+my]*matrix).sum()
            value = abs(value)
            new_array.append(value)
            
    return np.array(new_array).reshape(ax - mx + 1, ay - my + 1)
    

# 태블릿의 갤러리에 있는 사진 파일 경로
image_path = "CD\CD_2523_x020.jpg"

# 사진 불러오기
loaded_image = load_image(image_path)

# 사진의 픽셀 값을 2차원 배열에 저장
pixel_array = image_to_array(loaded_image)

#사진을 컨볼루션 행열과 합성 곱하여 새로운 이미지 생성
red_array = array_to_REDscale_array(pixel_array)
green_array = array_to_GREENscale_array(pixel_array)
blue_array = array_to_BLUEscale_array(pixel_array)

hWeight, vWeight = w, 0
Hred_array = convolut(red_array)
Hgreen_array = convolut(green_array)
Hblue_array = convolut(blue_array)

hWeight, vWeight = 0, w
Vred_array = convolut(red_array)
Vgreen_array = convolut(green_array)
Vblue_array = convolut(blue_array)

red_image_array = Hred_array + Vred_array
green_image_array = Hgreen_array + Vgreen_array
blue_image_array = Hblue_array + Vblue_array

image_array = []

ix, iy = np.shape(red_image_array)

for x in range(ix):
    temp = []
    for y in range(iy):
        temp.append([red_image_array[x][y], green_image_array[x][y], blue_image_array[x][y]])
    image_array.append(temp)
        
image_array = np.array(image_array).reshape(ix, iy, 3)

new_image = Image.fromarray(image_array.astype(np.uint8))

plt.imshow(new_image)
plt.show()

# 결과 확인
#print("사진 크기:", new_image.shape)
#print("픽셀 값:", new_image)
