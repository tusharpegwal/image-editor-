import imutils
import cv2 
image = cv2.imread("receipt.jpg")

(h, w, d) = image.shape 
print ("width = {}, height = {}, depth = {}" .format(w, h, d))
cv2.imshow("image" , image)
cv2.waitKey(0)
(B, G, R) = image[100,50]
print("R={}, G={}, B={}".format(R, G, B))
roi = image[100:500, 500:1000]
cv2.imshow("ROI", roi)
cv2.waitKey(0)
resized = cv2.resize(image, (800, 800))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)
r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)
resized = imutils.resize(image, width= 300)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)
rotated = imutils.rotate(image, -90)
cv2.imshow("image yahan show hogi", rotated)
cv2.waitKey(0)
rotated = imutils.rotate_bound(image, -45)
cv2.imshow("yahan pe bound k thorugh show hogi imutils version", rotated)
cv2.waitKey(0)
blured = cv2.GaussianBlur(image,(1,1),0)
cv2.imshow("yahan blure hoke aayega ", blured)
cv2.waitKey(0)
output = image.copy()
cv2.rectangle(output, (300, 200), (500, 600), (0, 0, 25), 2)
cv2.imshow("rectangle", output)
cv2.waitKey(0)
cv2.circle(output, (300,300), 20, (25, 0, 0), -1)
cv2.imshow("circle is here ", output)
cv2.waitKey(0)
output = image.copy()
cv2.putText(output, "yahan pe text hai ", (100, 500),
    cv2.FONT_HERSHEY_PLAIN, 20.0, (0, 25, 0), 2)
cv2.imshow("ye meri text wali file ", output)
cv2.waitKey(0)


