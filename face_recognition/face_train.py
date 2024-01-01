from imutils import paths  # imutils includes opencv functions
import face_recognition
import pickle
import cv2
import os

# get paths of each file in the folder named Images
# Images here contain data (folders of various people)
imagePath = list(paths.list_images('Images'))
kEncodings = []
kNames = []

# loop over the image paths
for (i, ip) in enumerate(imagePath):
    # extract the person's name from the image path
    name = ip.split(os.path.sep)[-2]

    # load the input image and convert it from BGR
    image = cv2.imread(ip)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    boxes = face_recognition.face_locations(rgb, model='hog')

    # compute the facial embedding for any face
    encodings = face_recognition.face_encodings(rgb, boxes)

    # loop over the encodings
    for encoding in encodings:
        kEncodings.append(encoding)
        kNames.append(name)

# save encodings along with their names in a dictionary
data = {"encodings": kEncodings, "names": kNames}

# use pickle to save data into a file for later use
with open("face_enc", "wb") as f:
    f.write(pickle.dumps(data))  # to open the file in write mode

