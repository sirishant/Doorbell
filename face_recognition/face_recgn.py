import face_recognition
import imutils  # imutils includes OpenCV functions
import pickle
import time
import cv2
import os

# To find the path of the XML file containing the HaarCascade file
cfp = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
# Load the HaarCascade in the cascade classifier
fc = cv2.CascadeClassifier(cfp)
# Load the known faces and embeddings saved in the last file
data = pickle.loads(open('face_enc', "rb").read())

# Find the path to the image you want to detect a face and pass it here
image = cv2.imread('AGC_20231222_195902284.MV.jpg')
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Convert the image to greyscale for HaarCascade
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = fc.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6, minSize=(60, 60), flags=cv2.CASCADE_SCALE_IMAGE)

# The facial embeddings for the face in the input
encodings = face_recognition.face_encodings(rgb)
names = []
# Loop over the facial embeddings in case
# we have multiple embeddings for multiple faces
for encoding in encodings:
    # Compare encodings with encodings in data["encodings"]
    # Matches contain an array with boolean values True and False
    matches = face_recognition.compare_faces(data["encodings"], encoding)
    # Set name = "Unknown" if no encoding matches
    name = "Unknown"
    # Check to see if we have found a match
    if True in matches:
        # Find positions at which we get True and store them
        matchedIdxs = [i for (i, b) in enumerate(matches) if b]
        count = {}
        # Loop over the matched indexes and maintain a count for
        # each recognized face
        for i in matchedIdxs:
            # Check the names at respective indexes we stored in matchedIdxs
            name = data["names"][i]
            # Increase count for the name we got
            count[name] = count.get(name, 0) + 1
        # Set the name which has the highest count
        name = max(count, key=count.get)
    # Will update the list of names
    names.append(name)
    print(names)

# Loop over the recognized faces
for ((x, y, w, h), name) in zip(faces, names):
    # Rescale the face coordinates
    # Draw the predicted face name on the image
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
    cv2.imshow("Frame", image)
    cv2.waitKey(0)
