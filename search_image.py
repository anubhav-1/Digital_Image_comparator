import cv2
import glob

def getFiles(folder_name) :
    files_list = []
    for filename in glob.glob(folder_name + '/*.jpg') :
        files_list.append(filename)
    return files_list    

def search(target_image_name, test_images) :
    target_img = cv2.imread(target_image_name)
    orb = cv2.ORB_create()
    
    kp, des = orb.detectAndCompute(target_img, None)
    keypoints = []
    descriptors = []
    for image_name in test_images :
        kp1, des1 = orb.detectAndCompute(cv2.imread(image_name), None)
        keypoints.append(kp1)
        descriptors.append(des1)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

    matches_list = []
    for i in range(0, len(descriptors)) :
        matches = bf.match(des, descriptors[i])
        matches = sorted(matches, key = lambda x:x.distance)
        matches_list.append(matches)

    values = []
    for i in range(0, len(matches_list)) :
        values.append(0)
        for j in range(0, 16) :
            values[i] += matches_list[i][j].distance

    min_index = 0
    for i in range(0, len(values)) :
        if(values[i] < values[min_index]) :
            min_index = i

    return test_images[min_index]


# img_path = search('2.JPG', getFiles('/home/sagar/python_programs/cv/data'))
# img = cv2.imread(img_path, 1)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()