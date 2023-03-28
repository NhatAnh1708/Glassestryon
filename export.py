
import cv2
from matplotlib import pyplot as plt

path ='eval_0/test0_warp5_it50000'

fig, axs = plt.subplots(2, 3)  # tạo 2 hàng 3 cột các ô subplot
img1=cv2.imread(f'{path}/image_g0_output.png')
img2=cv2.imread(f'{path}/image_g1_output.png')
img3=cv2.imread(f'{path}/image_g2_output.png')
img4=cv2.imread(f'{path}/image_g7_output.png')
img5=cv2.imread(f'{path}/image_g6_output.png')
img6=cv2.imread(f'{path}/image_g5_output.png')
# đọc và hiển thị hình ảnh trong từng ô subplot
axs[0, 0].imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
axs[0, 1].imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
axs[0, 2].imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
axs[1, 0].imshow(cv2.cvtColor(img4, cv2.COLOR_BGR2RGB))
axs[1, 1].imshow(cv2.cvtColor(img5, cv2.COLOR_BGR2RGB))
axs[1, 2].imshow(cv2.cvtColor(img6, cv2.COLOR_BGR2RGB))
plt.savefig('dataset/Figure.png')
plt.show()  # hiển thị các hình ảnh
