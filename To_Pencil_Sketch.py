import cv2

# reading image
image = cv2.imread("/Users/macbookpro/Desktop/To be converted to png sketch/Michelle-Monaghan_credit-Pulmanns.jpg")

#converting RGB to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray Image", gray_image)

#image inversion
inverted_image = 255 - gray_image
#cv2.imshow("Inverted Image", inverted_image)

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
#cv2.imshow("Blurred Image", blurred)

inverted_blurred = 255 - blurred
#cv2.imshow("Inverted blurred", inverted_blurred)

pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale = 256.0)

#cv2.imshow("Original Image", image)
#cv2.imshow("Pencil Sketch", pencil_sketch)
#cv2.waitKey(0)

cv2.imwrite("/Users/macbookpro/Desktop/Pencil Sketch of 20210908_165614-Enhanced.png", pencil_sketch)
