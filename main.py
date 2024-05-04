import cv2
import face_recognition

# Carrega a imagem
image = face_recognition.load_image_file("data/test2.jpeg")

# Localiza os rostos na imagem
face_locations = face_recognition.face_locations(image)

# Loop sobre as localizações dos rostos
for top, right, bottom, left in face_locations:
    # Recorta a região do rosto na imagem original
    face_image = image[top:bottom, left:right]
    face_image = cv2.cvtColor(face_image, cv2.COLOR_RGB2BGR)

    # Exibe a imagem do rosto recortado usando o OpenCV
    cv2.imshow('Face', face_image)
    cv2.waitKey(0)  # Espera por uma tecla para fechar a janela
    cv2.destroyAllWindows()