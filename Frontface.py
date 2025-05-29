import face_recognition

image = face_recognition.load_image_file("group.jpg")
face_locations = face_recognition.face_locations(image)  # detect all person position
face_encodings = face_recognition.face_encodings(image)  # extract coding feature
