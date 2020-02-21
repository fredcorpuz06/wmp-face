""" 
==========================
Recognize faces in 1 image
==========================

In this example, we will demonstrate how wmp-face finds faces in input
images, crop out a face thumbnail and predicts a name
"""

# Author: Frederick Corpuz <fcorpuz@wesleyan.edu>

from wmp import detect, utils


def main():
    FACE_COMP_THRES = 0.6
    ENCODED_REF_DIR = "wmp/datasets/reference-encoded"
    NEW_IMG = "wmp/datasets/sample_image.jpg"

    fd = detect.FaceDetector()
    fr = detect.FaceRecognizer(ENCODED_REF_DIR)

    face_image = detect.FaceImage(NEW_IMG)
    face_image = fd.find_faces(face_image)  # FaceImage

    face_image = fr.predict_names(face_image)
    print(face_image.retrieve_names())

    # TODO: return comparison matrix
    # TODO: write face thumbnails w/ predicted names


if __name__ == "__main__":
    main()
