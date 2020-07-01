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
    IMG = "wmp/datasets/sample_image.jpg"
    OUTDIR = "wmp/datasets/sample-facemarks/"

    fd = detect.FaceDetector()
    fr = detect.FaceRecognizer(ENCODED_REF_DIR)

    face_image = detect.FaceImage(IMG)
    face_image = fd.find_faces(face_image)  # `FaceImage` with results

    face_image = fr.predict_names(face_image, store_comparisons=True)

    print(face_image.retrieve_names())
    ns, distances = face_image.retrieve_comparisons()
    print(ns)
    print(distances)
    face_image.write_faces(OUTDIR)


if __name__ == "__main__":
    main()
