import cv2

'''
Load the haarcascade classifier. Give and abolute path if xml file is not found.
'''
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the image and store it in array.
# Give and abolute path if image file is not found
img = cv2.imread('stanbul.jpg')

# Convert image to gray scale for prediction.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''
  detectMultiScale function takes three input 
  ScaleFactor : How much the image size is reduced at each image scale. 
  MinNeighbors : How many ‘neighbors’ each candidate rectangle should have.
  MinSIze : The minimum object size. Default is (30, 30)

  This function returns the list of bounding box of each face found in image.

  For this example scaleFactor = 1.3 and MinNeighbors = 5
  Twik the parameter and see the results. 
'''

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Draw bounding box to imput image.
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()