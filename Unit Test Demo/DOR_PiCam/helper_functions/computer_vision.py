from PIL import Image
import cv2
import numpy as np

def percentage_color(image_file, t1, *color):
    
    img = cv2.imread(image_file)
    imgOrig = img.copy()
    img = change_brightness(img, 40)
    mainColor = color[0]
    
    boundaries = [([max(0, mainColor[2] - t1), max(0, mainColor[1] - t1), max(0, mainColor[0] - t1)],
                    [min(255, mainColor[2] + t1), min(255, mainColor[1] + t1), min(255, mainColor[0] + t1)])]
    
    (lower, upper) = boundaries[0]
    
    lower = np.array(lower, dtype = np.uint8)
    upper = np.array(upper, dtype = np.uint8)
    
    mask = cv2.inRange(img, lower, upper)
    
    cv2.imshow("Binary mask", mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    output = cv2.bitwise_and(img, img, mask = mask)
    
    cv2.imshow("ANDed mask", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    ratio_color = cv2.countNonZero(mask)/mask.size
    
    colorPercent = ratio_color * 100
    
    print("Color percentage:", np.round(colorPercent, 2))
    
    imgCombined = np.hstack([imgOrig, output])
    imgCombined = cv2.resize(imgCombined, (1080, 720))
    cv2.imshow("Image before and after", imgCombined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return colorPercent

def change_brightness(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v,value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img