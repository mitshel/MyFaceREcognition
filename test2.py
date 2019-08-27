import cv2
import dlib
import face_recognition

dlib.DLIB_USE_CUDA = True

# Get a reference to webcam
video_capture = cv2.VideoCapture(0)

image1 = face_recognition.load_image_file("faces/User.1.1.jpg")
face_encoding_1 = face_recognition.face_encodings(image1)[0]
image2 = face_recognition.load_image_file("faces/User.2.1.jpg")
face_encoding_2 = face_recognition.face_encodings(image2)[0]

known_faces = [
    face_encoding_1,
    face_encoding_2,
]

# Initialize variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0

while True:
    print('Read frame', frame_number)
    # Grab a single frame of video
    ret, frame = video_capture.read()
    frame_number += 1

    # Quit when the input video file ends
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    print('Find face locations')
    #face_locations = face_recognition.face_locations(rgb_frame, model="cnn")
    face_locations = face_recognition.face_locations(rgb_frame)
    print('Calculate face Encodings')
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_names = []

    print('Search faces')
    for face_encoding in face_encodings:

        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.70)

        name = None

        if match[0]:
            name = "Dmitry"
        else:
            name = "Artem"

        face_names.append(name)

    # Label the results
    print('Label results')
    for (top, right, bottom, left), name in zip(face_locations, face_names):

        if not name:
            continue

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX

        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()