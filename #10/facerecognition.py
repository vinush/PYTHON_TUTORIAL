import cv2
import dlib

# read the image
img = cv2.imread("img2.jpg")

# convert img to grayscale: 3d -> 2d
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

# dlib: Load face recognition detector
face_detector = dlib.get_frontal_face_detector()

# load the predictor
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


# use detector to find face landmarks
faces = face_detector(gray)
print(len(faces))

for face in faces:
    x1 = face.left()  # left point
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()  # bottom point

    # dra a rectangle
    cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=3)

    face_feature = predictor(image=gray, box=face)

    # loop through all 68 points
    for n in range(0, 68):
        x = face_feature.part(n).x
        y = face_feature.part(n).y

        # draw a circle
        cv2.circle(img=img, center=(x, y), radius=2, color=(0, 0, 255), thickness=1)


# show image
cv2.imshow(winname="Face Recognition App", mat=img)

# wait for a key press to exit
cv2.waitKey(delay=0)

# close all windows
cv2.destroyAllWindows()
