# Копирование фотографий где есть Дмитрий

import os
import shutil
import dlib
import face_recognition
from PIL import ImageFont, ImageDraw, Image

dlib.DLIB_USE_CUDA = True
fontsize = 50
font = ImageFont.truetype("arial.ttf", fontsize)


# Get a reference to webcam
photo_path = 'E:\\Photo'
photo_dest = 'E:\\Photo_DS\\1'

image1 = face_recognition.load_image_file("faces/User.1.1.jpg")
face_encoding_1 = face_recognition.face_encodings(image1)[0]
# image2 = face_recognition.load_image_file("faces/User.2.1.jpg")
# face_encoding_2 = face_recognition.face_encodings(image2)[0]

known_faces = [
    face_encoding_1,
    # face_encoding_2,
]

# Initialize variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0

for address, dirs, files in os.walk(photo_path):
    for file in files:
        body, ext = os.path.splitext(file)
        if ext.lower() in ('.jpg',',jpeg'):
            print('Find jpeg file ({})... Detecting...'.format(file))
            src_path = os.path.join(address, file)
            dest_path = os.path.join(photo_dest, file)
            image = face_recognition.load_image_file(src_path)
            print('Find Face locations')
            face_locations = face_recognition.face_locations(image, number_of_times_to_upsample = 0)
            print('Calculate Face Encodings')
            face_encodings = face_recognition.face_encodings(image, face_locations)

            face_names = []
            copy_flag = False

            print('Detected faces count: {}'.format(len(face_encodings)))

            # Просматриваем все лица
            for face_encoding in face_encodings:
                match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.60)

                name = None

                if match[0]:
                    print("File {} - find Dmitry Face...".format(src_path))
                    name = "Dmitry"
                    copy_flag = True
                    # shutil.copyfile(src_path, dest_path)
                else:
                    print("File {} - Not find Dmitry Face...".format(src_path))

                face_names.append(name)

            if copy_flag:
                for (top, right, bottom, left), name in zip(face_locations, face_names):

                    if not name:
                        continue

                    # Draw a box around the face
                    img_pil = Image.fromarray(image)
                    draw = ImageDraw.Draw(img_pil)
                    draw.rectangle(((left, top), (right, bottom)), outline='red', width=3)
                    # Draw the text
                    draw.text((left + 5, top - fontsize - 5), str(name), font=font,  fill='red')

                img_pil.save(dest_path)






