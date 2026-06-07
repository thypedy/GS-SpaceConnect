
import cv2


def inicializar_detector():
    """
    Carrega o modelo de detecção facial.
    """
    return cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )


def encontrar_camera():
    """
    Procura uma câmera disponível.
    """
    for i in range(5):

        camera = cv2.VideoCapture(i)

        if camera.isOpened():
            print(f"Camera encontrada no indice {i}")
            return camera

    return None


def detectar_astronautas(frame, detector):
    """
    Realiza a inferência visual.
    """

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces = detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )

    return faces


def desenhar_interface(frame, faces):

    astronautas = len(faces)

    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Astronauta",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    if astronautas > 0:
        status = "AREA MONITORADA"
        cor_status = (0, 255, 0)
    else:
        status = "ALERTA: AREA SEM ASTRONAUTAS"
        cor_status = (0, 0, 255)

    cv2.rectangle(
        frame,
        (0, 0),
        (frame.shape[1], 100),
        (40, 40, 40),
        -1
    )

    cv2.putText(
        frame,
        f"Astronautas Detectados: {astronautas}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        status,
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        cor_status,
        2
    )

    return frame


def main():

    detector = inicializar_detector()

    camera = encontrar_camera()

    if camera is None:
        print("Nenhuma camera encontrada.")
        return

    while True:

        ret, frame = camera.read()

        if not ret:
            print("Erro ao capturar imagem.")
            break

        faces = detectar_astronautas(
            frame,
            detector
        )

        frame = desenhar_interface(
            frame,
            faces
        )

        cv2.imshow(
            "SpaceConnect - Monitoramento de Astronautas",
            frame
        )

        tecla = cv2.waitKey(1)

        if tecla == 27:
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
