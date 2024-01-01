import face_recognition
import imutils
import pickle
import cv2
import os

def checkImg():
    cfp = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
    fc = cv2.CascadeClassifier(cfp)
    data = pickle.loads(open('face_enc', "rb").read())

    names = {}
    for name in data["names"]: # Set initial confidences as 0
        names[name] = 0
        names['Unknown'] = 0
    
    #for i in range(12): # 12 images
    image = cv2.imread(f"test_img2.jpg") # Check test_img0, 1, 2 etc
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = fc.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6, minSize=(60, 60), flags=cv2.CASCADE_SCALE_IMAGE)

    encodings = face_recognition.face_encodings(rgb)

    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "Unknown"
        confidence = 0

        if True in matches:
            face_distances = face_recognition.face_distance(data["encodings"], encoding)
            best_match_index = matches.index(True)
            confidence = 2 * (1 - face_distances[best_match_index]) * 100

            if confidence > 90:
                name = data["names"][best_match_index]

        names[name] += confidence
        
    print(names)
    return names        

# Define a function to display the image with rectangles
def display_image(image, faces, names):
    for ((x, y, w, h), (name, confidence)) in zip(faces, names):
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        display_text = f"{name} ({confidence:.2f}%)"
        cv2.putText(image, display_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    # Resize the window to fit within the display resolution
    cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Frame", 800, 600)  # Set the desired window size

    cv2.imshow("Frame", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the function to display the image after processing all faces
# display_image(image.copy(), faces, names)

if __name__ == '__main__':
    checkImg()


