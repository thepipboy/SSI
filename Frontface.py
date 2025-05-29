import face_recognition

image = face_recognition.load_image_file("group.jpg")
face_locations = face_recognition.face_locations(image)  # 检测所有人脸位置
face_encodings = face_recognition.face_encodings(image)  # 提取特征编码a