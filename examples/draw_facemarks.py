"""
================
Draw facemarks
================

In this example, we will demonstrate how wmp-face finds faces in input 
images, crops out a face thumbnail and
 draws "facemarks"

"""

# Author: Frederick Corpuz <fcorpuz@wesleyan.edu>

from wmp import detect, utils


def main():
    IMG = "wmp/datasets/sample_image.jpg"
    OUTDIR = "wmp/datasets/sample-facemarks/"

    fd = detect.FaceDetector()  # can be different detectors

    face_image = detect.FaceImage(IMG)
    face_image_results = fd.find_faces(face_image)

    face_image_results.write_faces(OUTDIR)
    # face_image_results.write_faces(OUTDIR, marked=True)


if __name__ == "__main__":
    main()
