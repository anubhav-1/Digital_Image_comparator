from tkinter.filedialog import askopenfilename
import cv2
import os
import search_image

filename = askopenfilename()
img_path = search_image.search(filename, search_image.getFiles(os.path.expanduser('~') + '/image_database'))
img = cv2.imread(img_path, 1)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()