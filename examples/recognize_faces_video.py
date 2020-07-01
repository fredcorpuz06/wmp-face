""" 
==========================
Recognize faces in 1 video
==========================

In this example, we will demonstrate how wmp-face finds faces in input
video, crop out a face thumbnail and predicts a name
"""

# Author: Frederick Corpuz <fcorpuz@wesleyan.edu>

from wmp import detect, utils
import cv2


def process_vid(vid_loc, fd, fr, down_factor):
    input_movie = cv2.VideoCapture(vid_loc)
    frame_number = 0
    rez = []
    while True:
        ret, frame = input_movie.read()
        frame_number += 1

        if not ret:
            break
        elif frame_number % down_factor != 0:
            continue

        face_image = detect.FaceImage(vid_loc, vid_frame=frame)
        face_image = fd.find_faces(face_image)
        face_image = fr.predict_names(face_image)
        face_image.retrieve_names()
        rez += face_image.true_names
        print(frame_number)

    input_movie.release()
    cv2.destroyAllWindows()

    return list(set(rez))


def main():
    FACE_COMP_THRES = 0.6
    ENCODED_REF_DIR = "wmp/datasets/reference-encoded"
    NEW_VID = "wmp/datasets/sample_video.mp4"
    DOWN_FACTOR = 30

    fd = detect.FaceDetector()
    fr = detect.FaceRecognizer(ENCODED_REF_DIR)

    names = process_vid(NEW_VID, fd, fr, DOWN_FACTOR)
    print(names)
    # TODO: return comparison matrix
    # TODO: write face thumbnails w/ predicted names


if __name__ == "__main__":
    main()
